import os
import re
import numpy as np
import pandas as pd
from helpers import slug
from sklearn import preprocessing

import seaborn as sns
import geopandas as gpd
import matplotlib.pyplot as plt

import plotly 
plotly.tools.set_credentials_file(username='tsadarah', api_key='fGstUNrmQhbpYD55Oth5')
import plotly.plotly as py
import plotly.graph_objs as go

import hvplot.pandas
import holoviews as hv
hv.extension('bokeh')


## World Map PLot for Diabetes Prevalence
datafilename = 'country_data.csv'
c = 'Diabetes Total per'
title = 'Percentage of Diabetic patients'
color = 'Blues'
plot_world_map(datafilename,c,title,color)

## World Map PLot for Overweight Prevalence
color = 'Wistia'
datafilename = 'country_data.csv'
c = 'Overweight Total per'
title = 'Percentage of Overweight Population'
cmap = 'Wistia'
plot_world_map(datafilename,c,title,cmap)


## Global Obesity vs Diabetes Correlation PLot 


## Risk Factors Radar Plot of Top 5 Countries & Average 
diab_data = pd.read_csv("diab.csv", usecols = ['Country/Region/World','ISO','Sex','Year','Age-standardised diabetes prevalence'])
bp_data = pd.read_csv("bp.csv", usecols = ['Country/Region/World','ISO','Sex','Year','Mean systolic blood pressure (mmHg)', 'Mean diastolic blood pressure (mmHg)'])
bmi_data = pd.read_csv("bmidata.csv", usecols = ['Country/Region/World','ISO','Sex','Year','Mean BMI'])

(df, diab) = cleanup_radar(diab_data,bp_data,bmi_data,"2014")
df_normalized = normalize_0to1(df)

max_prevelance = gender_prevelance(df,'men','maximum')
(data_max_prevalence, data_avg_max) = DataToPlot(diab, df_normalized, max_prevelance)

## Risk Factors Radar Plot of Lowest 5 Countries & Average 
min_prevelance = gender_prevelance(df,'men','minimum')
(data_min_prevelance, data_avg_min) = DataToPlot(diab, df_normalized, min_prevelance)

layout_max_prevalence = go.Layout(title='Related Risk Factors for 5 countries with Highest Diabetes Prevelence',font=dict(family='Arial', size=16, color='black'),
polar = dict(radialaxis = dict(visible = True,range = [0, 1])),showlegend = True)
fig = go.Figure(data=data_max_prevalence, layout=layout_max_prevalence)
py.iplot(fig)

layout_avg_max = go.Layout(title='Related Risk Factors for 5 countries with Lowest Diabetes Prevelence Averaged',font=dict(family='Arial', size=16, color='black'),
polar = dict(radialaxis = dict(visible = True,range = [0, 1])),showlegend = True)
fig = go.Figure(data=data_avg_max, layout=layout_avg_max)
py.iplot(fig)

layout = go.Layout(title='Related Risk Factors for 5 countries with Lowest Diabetes Prevelence',font=dict(family='Arial', size=16, color='black'),
polar = dict(radialaxis = dict(visible = True,range = [0, 1])),showlegend = True)
fig = go.Figure(data=data_min_prevelance, layout=layout)
py.iplot(fig)

layout_avg_min = go.Layout(title='Related Risk Factors for 5 countries with Lowest Diabetes Prevelence Averaged',font=dict(family='Arial', size=16, color='black'),
polar = dict(radialaxis = dict(visible = True,range = [0, 1])),showlegend = True)
fig = go.Figure(data=data_avg_min, layout=layout_avg_min)
py.iplot(fig)

## United States Map PLot for Diabetes Prevalence

## United States Map PLot for Obesity Prevalence

## United States Map PLot for Physical Inactivity Prevalence

## US Obesity vs Diabetes Correlation PLot

## US Physical Inactivity vs Diabetes Correlation PLot 

## Race Radar PLot

## Age vs Diabetes Prevalence PLots 

## Mean Age Trend in US Plot

## Income plot Income Group: Less than United States Average Income
less1 = pd.read_csv('income_data_less1.csv')
income_plot(less1).relabel('Income Group: Less than United States Average Income')

## Income plot Income Group: 1-3 times more than United States Average Income
one_three = pd.read_csv('income_data1_3.csv')
income_plot(one_three).relabel('Income Group: 1-3 times more than United States Average Income')

## Income plot Income Group: 3-5 times more than United States Average Income
three_five = pd.read_csv('income_data3_5.csv')
income_plot(three_five).relabel('Income Group: 3-5 times more than United States Average Income')

## Income plot Income Group: 5 time greater than United States Average Income
greater_5 = pd.read_csv('income_datag5.csv')
income_plot(greater_5).relabel('Income Group: 5 time greater than United States Average Income')