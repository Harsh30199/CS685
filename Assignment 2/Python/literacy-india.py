#!/usr/bin/env python
# coding: utf-8




import pandas as pd
import numpy as np





df = pd.read_csv('../Dataset/Literacy Total.csv')

df.head(50)





df1 = pd.read_csv('../Dataset/Bi and Tri Literacy2.csv', usecols=['State Code' , 'State Name' , 'Educational level' , 'Three Total'])


df1.head()





df2 = df.merge(df1,on=['State Code' , 'Educational level'],how='inner')

df2['percentage'] = np.round((df2['Three Total'] / df2['TOT_P'])*100,4)

df2.head(50)





data ={}
df4 = pd.DataFrame()

for i in range(36):
    
    df3 = df2[df2['State Code'] == i]
    
    data['State Code'] = i
    v = df3.iloc[df3.percentage.argmax(),0:].to_numpy().tolist()
    
    data['percentage'] = v[8]
    data['literacy-group'] = v[2]
    
    df4 =df4.append(data,ignore_index = True)
    
df4.head(50)
df4 = df4.rename(columns={'State Code' : 'state/ut'})
df4 = df4[['state/ut','literacy-group','percentage']]
df4.to_csv('../Output/literacy-india.csv',index = False) 

