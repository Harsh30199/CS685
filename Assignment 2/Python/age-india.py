#!/usr/bin/env python
# coding: utf-8




import pandas as pd
import numpy as np





df = pd.read_csv('../Dataset/Agewise Census.csv',usecols=['State Code','State Name','Age Group','TOT_P'])

df.head(50)





df1 = pd.read_csv('../Dataset/Bi and Tri Age2.csv', usecols=['State Code' , 'State Name' , 'Type' , 'Age Group' , 'Three Total'])

df1 = df1[df1['Type'] == 'Total']
df1.drop(df1.loc[df1['Age Group'] == 'Total'].index, inplace=True)
df1.drop(['Type'],axis='columns',inplace=True)
df1.head()





df2 = df.merge(df1,on=['State Code' , 'Age Group'],how='inner')

df2['percentage'] = np.round((df2['Three Total'] / df2['TOT_P'])*100,4)

df2.head(50)





data ={}
df4 = pd.DataFrame()

for i in range(36):
    
    df3 = df2[df2['State Code'] == i]
    
    data['State Code'] = i
    v = df3.iloc[df3.percentage.argmax(),0:7].to_numpy().tolist()
    
    data['percentage'] = v[6]
    data['age-group'] = v[2]
    
    df4 =df4.append(data,ignore_index = True)
    
df4.head(50)

df4 = df4.rename(columns={'State Code' : 'state/ut'})
df4 = df4[['state/ut','age-group','percentage']]
df4.to_csv('../Output/age-india.csv',index = False) 

