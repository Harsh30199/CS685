#!/usr/bin/env python
# coding: utf-8




import pandas as pd
import numpy as np





df = pd.read_csv('../Datasets Original/Literacy Census.csv')
df =df.dropna(axis='columns')
df.head()





data ={}
df2 = pd.DataFrame()
for i in range(36):

    data['State Code'] = i
    data['State Name'] = df[df['State Code'] == i]['State Name'].iloc[0]
    
    data['Educational level'] = 'Illiterate'
    data['TOT_P'] = df[df['State Code'] == i]['5'].iloc[0]
    data['TOT_M'] = df[df['State Code'] == i]['6'].iloc[0]
    data['TOT_F'] = df[df['State Code'] == i]['7'].iloc[0]
    
    df2 = df2.append(data,ignore_index = True)
    
    data['Educational level'] = 'Literate but below primary'
    data['TOT_P'] = df[df['State Code'] == i]['14'].iloc[0]
    data['TOT_M'] = df[df['State Code'] == i]['15'].iloc[0]
    data['TOT_F'] = df[df['State Code'] == i]['16'].iloc[0]
    
    df2 = df2.append(data,ignore_index = True)
    
    data['Educational level'] = 'Primary but below middle'
    data['TOT_P'] = df[df['State Code'] == i]['17'].iloc[0]
    data['TOT_M'] = df[df['State Code'] == i]['18'].iloc[0]
    data['TOT_F'] = df[df['State Code'] == i]['19'].iloc[0]
    
    df2 = df2.append(data,ignore_index = True)
    
    data['Educational level'] = 'Middle but below matric/secondary'
    data['TOT_P'] = df[df['State Code'] == i]['20'].iloc[0]
    data['TOT_M'] = df[df['State Code'] == i]['21'].iloc[0]
    data['TOT_F'] = df[df['State Code'] == i]['22'].iloc[0]
    
    df2 = df2.append(data,ignore_index = True)
    
    data['Educational level'] = 'Matric/Secondary but below graduate'
    data['TOT_P'] = df[df['State Code'] == i]['23'].iloc[0] + df[df['State Code'] == i]['26'].iloc[0] + df[df['State Code'] == i]['29'].iloc[0] + df[df['State Code'] == i]['32'].iloc[0]
    data['TOT_M'] = df[df['State Code'] == i]['24'].iloc[0] + df[df['State Code'] == i]['27'].iloc[0] + df[df['State Code'] == i]['30'].iloc[0] + df[df['State Code'] == i]['33'].iloc[0]
    data['TOT_F'] = df[df['State Code'] == i]['25'].iloc[0] + df[df['State Code'] == i]['28'].iloc[0] + df[df['State Code'] == i]['31'].iloc[0] + df[df['State Code'] == i]['34'].iloc[0]
    
    df2 = df2.append(data,ignore_index = True)
    
    data['Educational level'] = 'Graduate and above'
    data['TOT_P'] = df[df['State Code'] == i]['35'].iloc[0]
    data['TOT_M'] = df[df['State Code'] == i]['36'].iloc[0]
    data['TOT_F'] = df[df['State Code'] == i]['37'].iloc[0]
    
    df2 = df2.append(data,ignore_index = True)

df2 = df2[['State Code', 'State Name' , 'Educational level' , 'TOT_P' , 'TOT_M' , 'TOT_F']]

df2.to_csv('../Dataset/Literacy Total.csv' , index = False )

