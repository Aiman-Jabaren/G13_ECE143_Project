def required_imports():
    '''
    Import all the required libraries
    '''
    
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
    
    return