#!/usr/bin/env python
# coding: utf-8




import pandas as pd
import numpy as np





df = pd.read_csv('../Dataset/Census2.csv')

df1 = pd.read_csv('../Dataset/Bi and Tri Age2.csv')

df1 = df1[df1['Type']== 'Total']
df1 = df1[df1['Age Group'] == 'Total']

df1.head()





data ={}
df3 = pd.DataFrame()
for i in df1['State Code'] :
    data['State Code'] = i 
    data['State Name'] = df1[df1['State Code']== i]['State Name'].iloc[0]
    data['One Total'] = df[df['State Code']== i]['TOT_P'].iloc[0] - (df1[df1['State Code']== i]['Two Total'].iloc[0] + df1[df1['State Code']== i]['Three Total'].iloc[0])
    data['One Male'] = df[df['State Code']== i]['TOT_M'].iloc[0] - (df1[df1['State Code']== i]['Two Male'].iloc[0] + df1[df1['State Code']== i]['Three Male'].iloc[0])
    data['One Female'] = df[df['State Code']== i]['TOT_F'].iloc[0] - (df1[df1['State Code']== i]['Two Female'].iloc[0] + df1[df1['State Code']== i]['Three Female'].iloc[0])
    
    df3 = df3.append(data,ignore_index=True)

df3 = df3[['State Code', 'State Name' , 'One Total' , 'One Male' , 'One Female']]
df3.to_csv('../Dataset/Mono Gender.csv',index=False)

