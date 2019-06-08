# Diabetes: Analysis of Trends and Correlations

## Team Members
- Aiman Jabaren 
- Shashank John Peter Solomon
- Tejas Sadarahalli
- Treven Moore

## Problem:
Analysis of Diabetic Data to find different trends and correlations.

## Summary:
- Diabetes is one of the leading causes of death in the modern world. In order to fight diabetes, it needs to be studied and analyzed thoroughly. In this project, we have investigated diabetes statistics from different angles.
- We study diabetes prevalence around the globe and the reasons its prevalence varies, the risk factors of diabetes and the possible correlations with these risk factors.
- We also look into diabetes prevalence according to age and years, as well as the number of people with access to treatment across income groups and years.
We can summarize the following:
- It has very high correlation with obesity; It may cause obesity, vice versa, or they both share the same risk factors.
- It has very high correlation with lack of physical activity.
- Diabetes treatment and awareness varies according to income class and is violatile, likely due to the changing costs of healthcare.
- The average diabetic person's age rises with time which means the population as a whole is getting healthier.
- Diabetics are more likely to die before the age of 70 when compared to the rest of the population.
- Although both BMI and blood pressure are coorelated to diabetes, BMI is a much better metric to predict rates of diabetes in a population. This is especially true for populations with high rates of BMI.

## Methodology:
- After a diabetes overview research, we summarized the main points of interests for investigating diabetes.
- Different datasets and statistics were scrapped from national and international health organizations, such as the World Health   Organization and CDC
- We filtered the datasets according to credibility and relevancy
- We summarized the effectiveness of out datasets/ plots in answering our questions
- We have mainly used public Python libraries in order to process the data. 
- Some of the processing we have implemented included: calculating averages of diabetics and overweight population in different countries, calculated correlation between diabetes' possible risk factors, normalized risk factors per country and per county, plotted diabetes prevalence according to age and years and subdivided population into subgroups of diabetes treatment and awareness.
- We have used Python libraries and platfroms such as Geopandas, Bokeh, Matplotlib, Seaborn, Plotly and HoloViews in order to visualize and infer from the processed data

## Dataset:
We used statistics from World Health Organization (WHO), Center for Disease Control and Prevention (CDC) and others. The links to our dataset are:
```
        https://www.cdc.gov/diabetes/data/countydata/countydataindicators.html
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
|All the required imports are in the function 
|       - required_imports.py
|
|valid_cmap_d.py, helpers.py & desktop.ini - are used as helper file (dependency files) for plotting the geopandas world map plots accuratly
|
|To Plot the two world maps - Use Functions 
|       - download_pdf.py (to download PDFS from WHO site)
|       - read_pdf.py (to parse pdf files and compile a CSV dataset)
|       - plot_world_map.py (to plot World maps given data from excel spreadsheet. Reorganizes input data. It imports and matches countries' codes and locations to supplied data)  
|
|To Plot the Radar Plot for Related Risk Factors for 5 countries with Highest/Lowest Diabetes Prevelence and their averages - Use 
|functions
|       - cleanup_radar.py (clean up the loaded CSV files)
|       - normalize_0to1.py (normalize the data returned from cleanup_radar.py)
|       - gender_prevelance.py (Extract data once for Top 5 countries and once for bottom 5 countries using the data returned from normalize_0to1)
|       - DatToPlot.py (to plot radar plot using data returned from gender_prevelance.py)
|
|To Plot the three US Map - Use Functions 
|       - plot_us_maps.py (to plot US maps given data from excel spreadsheet. Reorganises input data. Returns plotly figure to be |plotted with plotly's plotting functions)    
|
|To Plot the correlations plots - Use Functions
|       - correlation_plot.py (to plot seaborn correlation plots between two given pd.Series)
|
|To Plot the radar plots for racial distribution - Use Functions
|       - plot_race_radar.py (to plot radar plots from CSV file, returns plotly figure to be plotted with plotly's plotting functions)
|
|To Plot age vs Diabetes Plots - Use Functions
|       - bar_plots_age.py (to plot bar plots of age distribution given age column from CSV file)
|
|To Plot mean age trends in US - Use Functions
|       - plot_mean_age.py (to plot line plot for mean age trend in US using data from bar_plots_age.py)
|
|To Plot the stacked bar plots for different income groups - Use Functions
|       - income_plot.py (to plot the stacked bar plot for every income group, after loading csv file)
```

## Instructions on Running Code:

-Python version: Python 3.6.6 64-bit

### Required Packages:

1. numpy
2. pandas
3. sklearn
4. BeautifulSoup
5. PyPDF2
6. pycountry

#### Plotting Packages

1. seaborn
2. geopandas
3. matplotlib.pyplot
4. plotly 
5. holoviews
6. hvplot.pandas

For installing these packages, you can use either pip to install packages. For example,

```
pip3 install numpy
```

if you are using anaconda you can use:

```
conda install numpy
```

### Run the code 

Run the appropriate functions for the plots you want by refering to the file structure section above.
