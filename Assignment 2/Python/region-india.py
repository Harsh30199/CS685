#!/usr/bin/env python
# coding: utf-8




import pandas as pd
import numpy as np





df = pd.read_csv('../Dataset/Mother Tongue Statewise.csv')
df.head()





df1 =pd.read_csv('../Dataset/regions.csv')





df = df.merge(df1, on = 'State Name')

df.drop(['State Code', 'State Name'],axis='columns',inplace = True)

df.head(100)





df2 = df.groupby(['Region','Language']).sum('Total')

df2.reset_index(inplace= True)
df2.head(500)





regions = ['North' ,'South', 'East' , 'West' , 'North-East' , 'Central']
data ={}

df4 = pd.DataFrame()

for r in regions:
    df3 = df2[df2['Region'] == r]
    v = df3.sort_values('Total' , inplace = False , ascending = False)['Language'][0:3]
    
    data['region'] = r
    data['language-1'] = v.iloc[0]
    data['language-2'] = v.iloc[1]
    data['language-3'] = v.iloc[2]
    
    df4 = df4.append(data,ignore_index=True)

df4 = df4[['region','language-1','language-2','language-3']]    

df4.sort_values('region',inplace=True)

df4.to_csv('../Output/region-india-a.csv',index=False)





df5 = pd.read_csv('../Dataset/Language Total Speakers Statewise.csv')
df5.head()





df5 = df5.merge(df1, on = 'State Name')

df5.drop(['State Code', 'State Name'],axis='columns',inplace = True)

df5.head(100)





df6 = df5.groupby(['Region','Language']).sum('Total')


df6.reset_index(inplace= True)
df6.head(500)





regions = ['North' ,'South', 'East' , 'West' , 'North-East' , 'Central']
data ={}

df8 = pd.DataFrame()

for r in regions:
    df7 = df6[df6['Region'] == r]
    v = df7.sort_values('Total' , inplace = False , ascending = False)['Language'][0:3]
    
    data['region'] = r
    data['language-1'] = v.iloc[0]
    data['language-2'] = v.iloc[1]
    data['language-3'] = v.iloc[2]
    
    df8 = df8.append(data,ignore_index=True)

df8 = df8[['region','language-1','language-2','language-3']]    

df8.sort_values('region',inplace=True)

df8.to_csv('../Output/region-india-b.csv',index=False)

