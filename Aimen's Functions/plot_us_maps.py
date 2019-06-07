import plotly.plotly as py
import plotly.figure_factory as ff
import plotly.graph_objs as go
from plotly.offline import plot, iplot
import numpy as np
import pandas as pd

def plot_map(df,low,high,title='Diabetes'):
    '''
    Function to plot US map given a dataframe. Low and high values need to be specified for the scale according to input data
    Title will be shown according to input
    
    :param: df
    :type: pd.DataFrame
    :param: low
    :type: int
    :param: high
    :type: int
    :param: title
    :type: str
    :return type: plotly plot
    '''
    assert isinstance(df,pd.DataFrame)
    assert isinstance(title,str)
    assert isinstance(low,int)
    assert isinstance(high,int)
    idxs = []
    # List of available years
    years = [2004,2005,2006,2007,2008,2009,2010,2011,2012,2013]

    # Find the column index for each year
    cls = list(df)
    for year in years:
        idxs.append(cls.index(year))

    # list of dataframes
    list_df = []
    for x,y in list(zip(idxs,years)):
        list_df.append(create_df(x,y,df))
    # Setting colorscale of the map
    colorscale = ["#deebf7","#c6dbef","#85bcdb","#57a0ce","#3082be","#1361a9","#0b4083"]
    # Endpoints of value scale
    endpts = list(np.linspace(low, high, len(colorscale) - 1))
    # FIPS codes
    fips = list_df[-1]['FIPS Codes'].astype(float).tolist()
    # Values
    temp = list_df[-1]['age-adjusted percent'].tolist()
    # If data is not available
    temp = [np.NaN if x=='No Data' else x for x in temp]
    values = temp

    fig = ff.create_choropleth(
        fips=fips, values=values,
        binning_endpoints=endpts,
        colorscale=colorscale,
        show_state_data=False,
        show_hover=False, centroid_marker={'opacity': 0},
        asp=2.9, title=title+' prevalence % in '+str(years[-1]),
        font=dict(family='Arial', color='black')
    )
    return iplot(fig, filename='choropleth_usa_'+title)
    
def create_df(idx,year,df):
    '''
    Function to create sub-dataframe for each year given column id and year
    
    :param: idx
    :type: int
    :param: year
    :type: int
    :param: df
    :type: pd.DataFrame
    :return type: pd.DataFrame
    '''
    assert isinstance(idx,int)
    assert isinstance(year,int)
    assert isinstance(df,pd.DataFrame)
    # First 3 columns are common
    f = df.iloc[:,0:3]
    # column names
    headers = f.iloc[0]
    # New dataframe with first row as columns headers
    fn = pd.DataFrame(f.values[1:], columns=headers)
    # Take 7 columns
    t = df.iloc[:,idx:idx+7]
    # Add a new column year
    t.loc[0,'year'] ='year'
    t.loc[1:,'year'] = year
    # add header
    headers = t.iloc[0]
    # Series to Dataframe
    new_df  = pd.DataFrame(t.values[1:], columns=headers)
    # Concatenate two dataframes
    new_df = pd.concat([fn,new_df],axis=1)
    return new_df

def get_df(df):
    '''
    Function to return list of dataframes after modifications from the original dataframe
    '''
    idxs = []
    # List of available years
    years = [2004,2005,2006,2007,2008,2009,2010,2011,2012,2013]

    # Find the column index for each year
    cls = list(df)
    for year in years:
        idxs.append(cls.index(year))

    # list of dataframes
    list_df = []
    for x,y in list(zip(idxs,years)):
        list_df.append(create_df(x,y,df))
    return list_df