def gender_prevelance(bmi,gender,prevelance):
    '''
    
    '''
    
    assert isinstance(bmi,pd.DataFrame)
    assert not bmi.empty
    assert 'Age-standardised diabetes prevalence' in bmi.columns
    
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