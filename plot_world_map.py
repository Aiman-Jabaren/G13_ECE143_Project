def plot_world_map(datafilename,c,title,cmap):
    '''
    Descitpion: Plots a heat map of a certain variable
            
        :Input Parameters: datafilename - name of data file (should be located in the same dirctory)
        :type: string
        :Input Parameters: c - name of data column (should start on line 1 in the csv file)
        :type: string
        :Input Parameters: title - title of plot
        :type: string
        :Input Parameters: cmap - color of heatmap
        :type: string
                    
        :Output Parameters: Plots a heatmap of the the world given 10 equal intervals of ranges             
    '''
    assert isinstance(datafilename, str) 
    assert isinstance(c, str) 
    assert isinstance(title, str) 
    assert isinstance(cmap, str) 
    assert valid_cmap_d(cmap) 
    
    datafile = os.path.expanduser(datafilename)   
    shapefile = os.path.expanduser('ne_10m_admin_0_countries_lakes/ne_10m_admin_0_countries_lakes.shp')
    
    n_colors = 10
    figsize = (16, 10)

    cols = ['Country', 'Country Code', c] # TODO switch with new col
    imgfile = 'img/{}.png'.format(slug(title))
    description = ''' '''.strip()
    
    gdf = gpd.read_file(shapefile)[['ADM0_A3', 'geometry']].to_crs('+proj=robin')
    gdf.sample(5)
    
    df = pd.read_csv(datafile,  usecols=cols)
    df.sample(5)
    
    merged = gdf.merge(df, left_on='ADM0_A3', right_on='Country Code')
    merged.describe()
    
    ax = merged.dropna().plot(column=c, cmap=cmap, figsize=figsize, scheme='equal_interval', k=n_colors, legend=True)
    color = '#CBC4C2'
    merged[merged.isna().any(axis=1)].plot(ax=ax, color=color)
    ax.set_title(title,fontname='Arial',  fontdict={'fontsize': 20}, loc='left')
    ax.annotate(description, xy=(0.1, 0.1), size=12, xycoords='figure fraction')
    ax.set_axis_off()
    ax.set_xlim([-1.5e7, 1.7e7])
    ax.get_legend().set_bbox_to_anchor((.12, .4))
    ax.get_figure()

    return