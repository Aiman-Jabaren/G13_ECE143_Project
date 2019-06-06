def DataToPlot(diab, bmi_normalized, max_prevelance):
    '''
    Descitpion: The Data of the top 5 countries or the bottom 5 countries 
    to be plotted as radar plot in plotly

        :Input Parameter: diab
        :type: Pandas Data frame
        :Input Parameter: bmi_normalized
        :type: Pandas Data frame
        :Input Parameter: max_prevelance
        :type: pandas.core.indexes.numeric.Int64Index
        
        :Output Parameter: data
        :type: List
        :Output Parameter: data_avg_max_min
        :type: List 
    '''
    
    assert isinstance(bmi_normalized,pd.DataFrame)
    assert isinstance(diab,pd.DataFrame)
    assert not bmi_normalized.empty
    assert not diab.empty
    
    mylst1 = bmi_normalized.values.tolist()[max_prevelance[0]] 
    country_name1 = diab.iloc[max_prevelance[0],1]

    mylst2 = bmi_normalized.values.tolist()[max_prevelance[1]] 
    country_name2 = diab.iloc[max_prevelance[1],1]

    mylst3 = bmi_normalized.values.tolist()[max_prevelance[2]] 
    country_name3 = diab.iloc[max_prevelance[2],1]

    mylst4 = bmi_normalized.values.tolist()[max_prevelance[3]] 
    country_name4 = diab.iloc[max_prevelance[3],1]

    mylst5 = bmi_normalized.values.tolist()[max_prevelance[4]] 
    country_name5 = diab.iloc[max_prevelance[4],1]
    
    avg = []
    for i in range(5):
        avg.append((mylst1[i]+mylst2[i]+mylst3[i]+mylst4[i]+mylst5[i])/5)
    
    ### Plotting
    data = [go.Scatterpolar(
              name = country_name1,
              r = mylst1,
              theta = ['BMI','Mean diastolic blood pressure','Mean systolic blood pressure','Diabetes prevalence','BMI'],
              line = dict(color = 'green')
            ),

            go.Scatterpolar(
            name = country_name2,
            r = mylst2,
            theta = ['BMI','Mean diastolic blood pressure','Mean systolic blood pressure','Diabetes prevalence','BMI'],
            line = dict(color = 'blue')
            ),

            go.Scatterpolar(
            name = country_name3,
            r = mylst3,
            theta = ['BMI','Mean diastolic blood pressure','Mean systolic blood pressure','Diabetes prevalence','BMI'],
            line = dict(color = 'red')
            ),

            go.Scatterpolar(
            name = country_name4,
            r = mylst4,
            theta = ['BMI','Mean diastolic blood pressure','Mean systolic blood pressure','Diabetes prevalence','BMI'],
            line = dict(color = 'yellow')
            ),

            go.Scatterpolar(
            name = country_name5,
            r = mylst5,
            theta = ['BMI','Mean diastolic blood pressure','Mean systolic blood pressure','Diabetes prevalence','BMI'],
            line = dict(color = 'orange')
            ),
            ]
    
    ### Plotting for average
    data_avg_max_min = [go.Scatterpolar(
        name = 'Average',
        r = avg,
        theta = ['BMI','Mean diastolic blood pressure','Mean systolic blood pressure','Diabetes prevalence','BMI'],
        line = dict(color = 'green')
        )]
    
    return data, data_avg_max_min