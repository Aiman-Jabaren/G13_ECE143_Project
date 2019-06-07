def normalize_0to1(bmi):
    '''
    
    '''
    
    assert isinstance(bmi,pd.DataFrame)
    assert not bmi.empty
    
    x = bmi.iloc[:,5:9].values # Returns a numpy array
    min_max_scaler = preprocessing.MinMaxScaler() # Normalizing
    x_scaled = min_max_scaler.fit_transform(x) # Normalizing
    bmi_normalized = pd.DataFrame(x_scaled) # Normalizing
    bmi_normalized['4'] = bmi_normalized[0] # Circulating the first colum to the last for radar plot
    
    return bmi_normalized