def income_plot(df):
    '''
    Descitpion: PLots the data for different income groups.The plots are 
    Stacked Bar Plot for four different groups with the Year along 
    the x-axis and Diabetes Prevelance on the y-axis. 

        :Input Parameter: df
        :type: Pandas Data frame
        
        :Output Parameter: Chart
        :type: Holoviews Bar Plot Object
    '''
    
    assert isinstance(df,pd.DataFrame)
    assert not df.empty
    assert 'Year' in df.columns
    assert 'Type' in df.columns
    assert 'Prevalence' in df.columns
    
    df.rename(str.lower, axis='columns')

    %opts Bars [tools=['hover'],legend_position='left',color_index='Variable',width=900,height=400](alpha=0.5,color=hv.Palette('Category20'))
    
    chart = df.groupby(['Year','Type'])['Prevalence'].sum().unstack()\
                .hvplot.bar(stacked=True,ylabel='Percentage (%)')\
                .redim(value=hv.Dimension('value',label='Prevalence',range=(0,105)))
    return chart