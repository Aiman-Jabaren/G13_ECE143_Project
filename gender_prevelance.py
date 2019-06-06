def gender_prevelance(bmi,gender,prevelance):
    '''
    Descitpion: Returns the relevent rows indices from the processed data frame of 
    the top 5 countries or the bottom 5 countries in terms of diabetes for 
    the gender specified.

        :Input Parameter: bmi
        :type: Pandas Data frame
        :Input Parameter: gender
        :type: Pandas Data string
        :Input Parameter: prevelance
        :type: Pandas Data string
        
        :Output Parameter: percent
        :type: pandas.core.indexes.numeric.Int64Index
    '''
    
    assert isinstance(bmi,pd.DataFrame)
    assert not bmi.empty
    assert 'Age-standardised diabetes prevalence' in bmi.columns
    assert gender in {'men','women'}
    assert prevelance in {'maximum','minimum'}
    
    if gender == 'men':
        bmi_men = bmi.iloc[:200] #0:200 for men 
        if prevelance == 'maximum':
            percent = bmi_men.nlargest(5,'Age-standardised diabetes prevalence').index # Get the country indices for 5 countries with the lowest prevelance
        else:
            percent = bmi_men.nsmallest(5,'Age-standardised diabetes prevalence').index # Get the country indices for 5 countries with the lowest prevelance
    else:
        bmi_women = bmi.iloc[200:] #200: for women
        if prevelance == 'maximum':
            percent = bmi_women.nlargest(5,'Age-standardised diabetes prevalence').index # Get the country indices for 5 countries with the lowest prevelance
        else:
            percent = bmi_women.nsmallest(5,'Age-standardised diabetes prevalence').index # Get the country indices for 5 countries with the lowest prevelance
        
    return percent