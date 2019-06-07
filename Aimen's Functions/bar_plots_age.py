import numpy as np
import pandas as pd
import holoviews as hv

def process_ages(age_df):
    '''
    Function to collect data into agewise bins. Gives percentage of diabetic people of certain age group
    
    :param: age_df
    :type: column of dataframe or series
    :returns: list
    
    Examples:
    If out of 10 diabetic people, 5 of those are in the age group 50-60 years and 4 in age group 60-70
    >>>process_ages(age)
    [('50-60',50),('60-70',40)]
    '''
    assert isinstance(age_df,(pd.DataFrame,pd.Series))
    assert not age_df.empty
    # Create bins for ages
    i = range(0,100,10)
    j = range(10,110,10)
    bins = list(zip(i,j))
    
    bin_count = []
    
    # DataFrame to numpy array
    age = age_df.values
    
    # Assign number of people to each age bin
    for x in bins:
        bin_count.append(np.count_nonzero((age>=x[0])&(age<x[1])))
    bin_count = np.asarray(bin_count,dtype = np.float32)

    # Total size of the dataset - also the size of the age column
    total_age = age.size
    
    # Divide each age bin by total number to get percentage
    bin_count = (bin_count/total_age)*100
    
    # String representation of bins
    str_bins = []
    for x in bins:
        str_bins.append(str(x[0])+'-'+str(x[1]))
    data = list(zip(str_bins,bin_count))
    
    # Calculate mean age
    mean_age = age.mean()
    
    return data,mean_age

def draw_age(data,year):
    '''
    Function to graw bar graph given data and year. Year is used in title
    
    :param: data
    :type: list
    :param: year
    :type: string
    :returns: holoviews plot
    '''
    assert isinstance(year,str)
    assert isinstance(data,list)
    # Plot the bars
    bars = hv.Bars(data,hv.Dimension('Age (in yrs)'),hv.Dimension('%population', range=(0, 30)))
    
    # Rotate x labels, set color, transparency and width
    bars.opts(xrotation=45,color='green',width=400, alpha=0.8)
    
    # Set title and fonts, use year in title
    bars.opts(title='Age vs Diabetes prevalence in '+year,fontsize={'title': 14, 'labels': 12, 'xticks': 10, 'yticks': 10})
    
    return bars

def age_to_int(x):
    '''
    Function to convert age in string to age in int
    To be used in vectorize for numpy array
    '''
    assert isinstance(x,str)
    # some ages had trailing spaces
    x = int(x.split()[0])
    return x

def process_ages_older(age_df):
    '''
    Function to collect data into agewise bins similar to above function but input dataframe here has 
    age values of string type. Also returns mean age of diabetic people
    
    :param: age_df
    :type: column of dataframe or series
    :returns: tuple
    :output1: list of data in bins
    :output2: mean age
    
    Examples:
    If out of 10 diabetic people, 5 of those are in the age group 50-60 years and 4 in age group 60-70
    >>>process_ages(age)
    [('50-60',50),('60-70',40)]
    '''
    assert isinstance(age_df,(pd.DataFrame,pd.Series))
    assert not age_df.empty
    # Create bins for ages
    i = range(0,100,10)
    j = range(10,110,10)
    bins = list(zip(i,j))
    bin_count = []
    
    # DataFrame to numpy array
    age = age_df.values
    
    # Vectorize age_to_int to operate on whole numpy array
    vf = np.vectorize(age_to_int)
    # Apply vectorized function on numpy array
    age = vf(age)
    
    # Assign number of people to each age bin
    for x in bins:
        bin_count.append(np.count_nonzero((age>=x[0])&(age<x[1])))
    bin_count = np.asarray(bin_count,dtype = np.float32)
    
    # Total size of the dataset - also the size of the age column
    total_age = age.size
    
    # Divide each age bin by total number to get percentage
    bin_count = (bin_count/total_age)*100
    
    # String representation of bins
    str_bins = []
    for x in bins:
        str_bins.append(str(x[0])+'-'+str(x[1]))
    data = list(zip(str_bins,bin_count))
    
    # Calculate mean age
    mean_age = age.mean()
    
    return data,mean_age