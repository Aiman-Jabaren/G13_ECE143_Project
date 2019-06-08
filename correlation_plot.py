import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation(x,y,title,xlabel=None,ylabel=None,blank='dots'):
    '''
    Funciton to plot correlation plots in seaborn
    
    :param: x
    :type: pandas DataFrame
    
    :param: y
    :type: pandas DataFrame
    
    :param: title
    :type: str
    
    :param: xlabel
    :type: str
    
    :param: ylabel
    :type: str
    
    :param: blank
    :values: dots/str
    :type: str
    
    :returns: seaborn plot
    '''
    assert isinstance(x,(pd.DataFrame,pd.Series))
    assert not x.empty
    assert isinstance(y,(pd.DataFrame,pd.Series))
    assert not y.empty
    assert isinstance(title,str)
    assert isinstance(xlabel,str)
    assert isinstance(ylabel,str)
    assert isinstance(blank,str)
    assert blank=='dots' or blank=='str'
    
    # Data is marked differently in different data sets
    # dots - missing data is marked as . . .
    # str - missing data is marked as "No Data"
    # Replace missing data with numpy NaN
    if blank is 'dots':
        x = x.apply(lambda x: np.NaN if x=='. . .' else float(x[:-1]))
        y = y.apply(lambda x: np.NaN if x=='. . .' else float(x[:-1]))
    elif blank is 'str':
        x = x.apply(lambda x: np.NaN if type(x)==str else float(x))
        y = y.apply(lambda x: np.NaN if type(x)==str else float(x))
    # To set font 
    afont = {'fontname':'Arial'}
    # Plot the seaborn regression plot
    ax = sns.regplot(x,y,fit_reg=True).set_title(title,**afont)
    # Add axis labels
    if xlabel and ylabel:
        axes = ax.axes
        axes.set_xlabel(xlabel,**afont)
        axes.set_ylabel(ylabel,**afont)
    # Y axis should start at 0
    axes.set_ylim(0,)
    return ax
