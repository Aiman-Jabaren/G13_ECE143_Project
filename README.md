# Diabetees: Analysis of Trends and Correlations

## Team Members
- Aiman Jabaren 
- Shashank John Peter Solomon
- Tejas Sadarahalli
- Treven Moore

## Problem:
Analysis of Diabetic Data to find different trends and correlation

## Summary:
- Diabetes is one of the leading causes of death in the modern world. In order to fight diabetes, it needs to be studied and analyzed thoroughly. In this project, we have investigated diabetes statistics from different angles.
- We study diabetes prevalence in the globe and the reasons its prevalent varies, the risk factors of diabetes and the possible correlations with these risk factors. We also look into diabetes prevalence according to age and years. 
We can summarize the following:
- It has very high correlation with Obesity; It may cause Obesity, vice versa or that they both share the same risk factors.
- It has very high correlation with physical activity.
- Diabetes treatment and awareness varies according to income class
- The average diabetic person's age rises with time which means the population as whole is getting healthier.
- Diabetics are more likely to die before the age of 70 when compared to the rest of the population.

## Methodology:
- After a diabetes overview research, we summarized the main points of interests for investigating diabetes.
- Different datasets and statistics were scrapped from national and international health organization, such as: World Health   Organization and CDC
- We filtered the datasets according to credibility and interest
- We summarized the possible datasets/ plots we need in order to answer the questions
- We have mainly used public Python libraries in order to process the data. 
- Some of the processing we have implemnted was: calculating averages of diabetics and overweight population in different countries, calculated correclation between diabetes possible risk factors, normalized risk factors per country and per county, plotted diabetes prevalence according to age and years and subdivided population into subgroups of diabetes treatment and awareness.
- We have used Python libraries and platfroms such as Geopandas, Bokeh, Matplotlib, Seaborn, Plotly and HoloViews in order to visualize and infer from the processed data
- 
## Dataset:
Statistics from World Health Organization (WHO), Center for Disease Control and Prevention (CDC) the links to the our dataset are:
```
        https://www.cdc.gov/nchs/nhis/nhis_2017_data_release.htm
        https://www.cdc.gov/diabetes/statistics/slides/long_term_trends.pdf
        https://www.medicalnewstoday.com/articles/318472.php
        https://catalog.data.gov/dataset?tags=diabetes
        https://mchb.hrsa.gov/whusa13/health-status/health-indicators/p/diabetes.html
        https://data.world/health/diabetes-prevalence/workspace/file?filename=rows.csv
        https://letsgethealthy.ca.gov/goals/living-well/decreasing-diabetes-prevalence/#_data-snapshot
        https://towardsdatascience.com/machine-learning-for-diabetes-562dd7df4d42
        https://www.who.int/diabetes/country-profiles/en/
        https://data.worldbank.org/indicator/sh.sta.diab.zs
        http://publichealthintelligence.org/content/prevalence-diabetes-world-2013
        https://healthmetrics.heart.org/prevalence-of-prediabetes-and-diabetes-in-the-united-states-1999-2016-stacked-bar-graph/
        http://ncdrisc.org/multiple-factors.html
        https://healthmetrics.heart.org/prevalence-of-prediabetes-and-diabetes-in-the-united-states-1999-2016-stacked-bar-graph/
```
## File Structure:

```
Root
|
+----Bokeh_images
     (contains images for bokeh/holoviws plots, The holviews plot from the income_plot.py get saved to this folder)
|
+----ne_10m_admin_0_countries_lakes
|    (contains the required files for the world map's geopandas plot)
|
|To Plot the two world maps - Use Functions 
|
|To Plot the Radar PLot for Related Risk Factors for 5 countries with Highest/Lowest Diabetes Prevelence and their averages - Use 
|functions
|       - cleanup_radar.py (clean up the loaded CSV files)
|       - normalize_0to1.py (normalize the data returned from cleanup_radar.py)
|       - gender_prevelance.py (Extract data once for Top 5 countries and once for bottom 5 countries using the data returned fro normalize_0to1)
|       - DatToPlot.py (to plot radar plot using data returned from gender_prevelance.py)
|
|To Plot the three US Map - Use Functions 
|
|To Plot the correlations plots - Use Functions
|
|To Plot the radar plots for racial distribution - Use Functions
|
|To Plot age vs Diabetes Plots - Use Functions
|
|To Plot the stacked bar plots for different income groups - Use Functions
|
```

## Instructions on Running Code:

-Python version: Python 3.6.6 64-bit

### Required Packages:

1. numpy
2. pandas
3. sklearn 

#### Plotting Packages

1. Seaborn
2. geopandas
3. matplotlib.pyplot
4. plotly 
5. holoviews
6. hvplot.pandas

For installing these packages, you can use either pip to install packages. For example,

```
pip3 install numpy
```

if your using anaconda you can use:

```
conda install numpy
```

### Run the code 
