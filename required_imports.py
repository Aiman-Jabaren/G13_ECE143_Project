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
    import plotly.plotly as py
    import plotly.io as pio
    import plotly.graph_objs as go
    from IPython.display import Image
    from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
    init_notebook_mode(connected=True)
    
    import hvplot.pandas
    import holoviews as hv
    hv.extension('bokeh')
    
    return