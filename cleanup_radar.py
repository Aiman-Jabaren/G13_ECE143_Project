def cleanup_radar(diab_data,bp_data,bmi_data,year = "2014"):
    '''
    Descitpion: Cleans up raw data from csv files and return a pandas data frame
    which has all the relevent columns from the differnt csv files for the data 
    pertaining to a certain Year. 

        :Input Parameter: diab_data
        :type: Pandas Data frame
        :Input Parameter: bp_data
        :type: Pandas Data frame
        :Input Parameter: bmi_data
        :type: Pandas Data frame
        :Input Parameter: year
        :type: Pandas Data string
        
        :Output Parameter: bmi
        :type: Pandas Data frame   
    '''
    
    assert isinstance(diab_data,pd.DataFrame)
    assert isinstance(bp_data,pd.DataFrame)
    assert isinstance(bmi_data,pd.DataFrame)
    assert isinstance(year,str)
    
    assert not diab_data.empty
    assert not bp_data.empty
    assert not bmi_data.empty
    
    assert 'Year' in diab_data.columns
    assert 'Year' in bp_data.columns
    assert 'Year' in bmi_data.columns
    
    assert 'Mean diastolic blood pressure (mmHg)' in bp_data.columns
    assert 'Mean systolic blood pressure (mmHg)' in bp_data.columns
    assert 'Age-standardised diabetes prevalence' in diab_data.columns
    
    diab = diab_data.loc[diab_data["Year"] == int(year)].reset_index() # Filtering out the dataframe only for the year you want 
    bp = bp_data.loc[bp_data["Year"] == int(year)].reset_index() # Filtering out the dataframe only for the year you want 
    bmi = bmi_data.loc[bmi_data["Year"] == int(year)].reset_index() # Filtering out the dataframe only for the year you want 

    bmi['Mean diastolic blood pressure (mmHg)'] = pd.Series(bp['Mean diastolic blood pressure (mmHg)']) # Appending Colums from different CSV to the bmi CSV
    bmi['Mean systolic blood pressure (mmHg)'] = pd.Series(bp['Mean systolic blood pressure (mmHg)']) # Appending Colums from different CSV to the bmi CSV
    bmi['Age-standardised diabetes prevalence'] = pd.Series(diab['Age-standardised diabetes prevalence']) # Appending Colums from different CSV to the bmi CSV

    return bmi, diab