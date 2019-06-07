import holoviews as hv

def plot_mean_age(years,mean_ages):
    '''
    Function to plot mean age data given a list of mean_ages and list of years
    
    :param: mean_ages
    :type: list
    :param: years
    :type: list
    :returns: holoviews plot
    '''
    assert isinstance(mean_ages,list)
    assert isinstance(years,list)
    assert len(years)>0
    assert len(mean_ages)>0
    assert all(i>=0 for i in mean_ages)
    assert all(i>=0 for i in years)
    assert all(isinstance(i,float) for i in mean_ages)
    assert all(isinstance(i,int) for i in years)
    # mean ages
    y = mean_ages
    # years
    x = years
    # create tuples
    d = list(zip(x,y))
    # Draw a scatter plot
    s = hv.Scatter(d,hv.Dimension('Year'),'Mean age').opts(size=8,tools=['hover'],title='Mean age of diabetics in US')
    # Draw a line
    c = hv.Curve(d,hv.Dimension('Year'),'Mean age')
    # Overlay both and return
    return s*c