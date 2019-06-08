import plotly.plotly as py
import plotly.figure_factory as ff
import plotly.graph_objs as go
from plotly.offline import plot, iplot
import numpy as np
import pandas as pd

def plot_race_radar(df,year,color):
    '''
    Function to plot race data in rada plot format given a year
    
    :param: df
    :type: pd.DataFrame
    :param: year
    :type: str
    :param: color
    :type: str
    :returns: plotly figure
    '''
    assert isinstance(df,pd.DataFrame)
    assert isinstance(year,str)
    assert isinstance(color,str)
    assert not df['LACHRC10'].empty
    # Filter for diabetic people
    dia = df.loc[df['LACHRC10']==1]
    # codes for races
    # 1-White,2-Black,6-Chinese,12-Indiam
    r = [1,2,6,12]
    # Empty list to store percentage of diabetics of each race 
    v = []
    # For each race
    for x in r:
        # For White people
        if x==1:
            # Filter for non diabetic
            normal = df.loc[df['MRACBPI2']==x]
            # Filter for hispanic
            hisp_norm = normal.loc[normal['ORIGIN_I']==1]
            # Filter for non hispanic
            wh_norm = normal.loc[normal['ORIGIN_I']==2]
            # Filter for diabetic 
            num_dia = dia.loc[dia['MRACBPI2']==x]
            # Filter for hispanic
            hisp_dia = num_dia.loc[num_dia['ORIGIN_I']==1]
            # Filter for non hispanic
            wh_dia = num_dia.loc[num_dia['ORIGIN_I']==2]
            # Percentage non hispanic
            per = len(wh_dia.index)/len(wh_norm.index)
            # Percentage hispanic
            per_h = len(hisp_dia.index)/len(hisp_norm.index)
            per = per*100
            per_h = per_h*100
            # Add to list 
            v.append([per,per_h])
        else: # for other non white races
            # Non diabetic 
            normal = df.loc[df['MRACBPI2']==x]
            # Diabetic
            num_dia = dia.loc[dia['MRACBPI2']==x]
            # Percentage
            per = len(num_dia.index)/len(normal.index)
            v.append(per*100)
    # Flattening because first element is a list
    v = flatten(v)
    # Looping back for radar plot
    v.append(v[0])
            
    # 3 Radial scatter plots, one for each year
    data = [go.Scatterpolar(
      name = year,
      r = v, # data
      # lood around to close the radar plot area
      theta = ['White','Hispanic','Black','Chinese','Indian','White'], # axis names 
      fill = 'toself',
      fillcolor=color,
      opacity=0.5,
      line = dict(
            color = color)
    )      ]

    layout = go.Layout(
      title='<b>Racial Distribution % in '+year+' </b>',
      font=dict(family='Arial', size=16, color='black'),
      polar = dict(
        radialaxis = dict(
          visible = True,
          range = [0, 2.5] # Axis range
        )
      ),
      showlegend = False
    )

    # Plot the fiure
    fig = go.Figure(data=data, layout=layout)
    return fig
            
def flatten(x):
    '''
    Function to flatten a list
    '''
    assert isinstance(x,list)
    o = []
    for i in x:
        if type(i) is list:
            for t in i:
                o.append(t)
        else:
            o.append(i)
    return o

def plot_race_radar_older(df,year,color):
    '''
    Function to plot race data in rada plot format given a year for older dataset files. 
    Since data format is different in the older files
    
    :param: df
    :type: pd.DataFrame
    :param: year
    :type: str
    :param: color
    :type: str
    :returns: plotty plot
    '''
    assert isinstance(df,pd.DataFrame)
    assert isinstance(year,str)
    assert isinstance(color,str)
    assert not df['LACHRC10'].empty
    # Filter for diabetic people
    dia = df.loc[df['LACHRC10']=='1 Chronic']
    # codes for races
    r = ['01 White' ,'02 Black/African American', '06 Chinese', '12 Asian Indian']
    # Empty list to store percentage of diabetics of each race
    v = []
    # For each race
    for x in r:
        # For White people
        if x=='01 White':
            # Filter for non diabetic
            normal = df.loc[df['MRACBPI2']==x]
            # Filter for hispanic
            hisp_norm = normal.loc[normal['ORIGIN_I']=='1 Yes']
            # Filter for non hispanic
            wh_norm = normal.loc[normal['ORIGIN_I']=='2 No']
            # Filter for diabetic
            num_dia = dia.loc[dia['MRACBPI2']==x]
            # Filter for hispanic
            hisp_dia = num_dia.loc[num_dia['ORIGIN_I']=='1 Yes']
            # Filter for non hispanic
            wh_dia = num_dia.loc[num_dia['ORIGIN_I']=='2 No']
            # Percentage non hispanic
            per = len(wh_dia.index)/len(wh_norm.index)
            # Percentage hispanic
            per_h = len(hisp_dia.index)/len(hisp_norm.index)
            per = per*100
            per_h = per_h*100
            # Add to list 
            v.append([per,per_h])
        else: # for other non white races
            # Non diabetic
            normal = df.loc[df['MRACBPI2']==x]
            # Diabetic
            num_dia = dia.loc[dia['MRACBPI2']==x]
            # Percentage
            per = len(num_dia.index)/len(normal.index)
            # Add to list
            v.append(per*100)
    # Flattening because first element is a list
    v = flatten(v)
    # Looping back for radar plot
    v.append(v[0])
            
    # 3 Radial scatter plots, one for each year
    data = [go.Scatterpolar(
      name = year,
      r = v, # data
      # lood around to close the radar plot area
      theta = ['White','Hispanic','Black','Chinese','Indian','White'], # axis names 
      fill = 'toself',
      fillcolor=color,
      opacity=0.5,
      line = dict(
            color = color)
    )      ]

    layout = go.Layout(
      title='<b>Racial Distribution % in '+year+' </b>',
      font=dict(family='Arial', size=16, color='black'),
      polar = dict(
        radialaxis = dict(
          visible = True,
          range = [0, 2.5] # Axis range
        )
      ),
      showlegend = False
    )

    # Plot the fiure
    fig = go.Figure(data=data, layout=layout)
    return fig
