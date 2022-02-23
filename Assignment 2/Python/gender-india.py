#!/usr/bin/env python
# coding: utf-8




import pandas as pd
import numpy as np

from scipy import stats





df = pd.read_csv('../Dataset/Census2.csv')

df1 = pd.read_csv('../Dataset/Bi and Tri Age2.csv')
df1 = df1[df1['Type']=='Total']
df1 = df1[df1['Age Group']=='Total']


df2 = df1.merge(df,on='State Code',how='inner')
df2['male-to-female-ratio-2'] = np.round(df2['Two Male']/ df2['Two Female'],4)
df2['male-to-female-ratio-3'] = np.round(df2['Three Male']/ df2['Three Female'],4)
df2['male-to-female-ratio-1'] = np.round((df2['TOT_M']-df2['Two Male']-df2['Three Male'])/ (df2['TOT_F']-df2['Two Female']-df2['Three Female']),4)
df2['male-percentage-3'] = np.round((df2['Three Male'] / df2['TOT_M'])*100,4)
df2['female-percentage-3'] = np.round((df2['Three Female'] / df2['TOT_F'])*100,4)
df2['male-percentage-2'] = np.round((df2['Two Male'] / df2['TOT_M'])*100,4)
df2['female-percentage-2'] = np.round((df2['Two Female'] / df2['TOT_F'])*100,4)
df2['male-percentage-1'] = np.round(((df2['TOT_M']-df2['Two Male']-df2['Three Male']) / df2['TOT_M'])*100,4)
df2['female-percentage-1'] = np.round(((df2['TOT_F']-df2['Two Female']-df2['Three Female']) / df2['TOT_F'])*100,4)
df2['male-to-female'] = np.round(df2['TOT_M']/df2['TOT_F'],4)
df2['t-test'],df2['p-value'] = stats.ttest_1samp([df2['male-to-female-ratio-3'],df2['male-to-female-ratio-2'],df2['male-to-female-ratio-1']],df2['male-to-female'])
df2['p-value'] = np.round(df2['p-value'],4)

df3 = df2[['State Code','male-percentage-3','female-percentage-3','p-value']]
df3 = df3.rename(columns= {'State Code':'state-code','male-percentage-3':'male-percentage','female-percentage-3':'female-percentage'})
df3.to_csv('../Output/gender-india-c.csv',index =False)


df4 = df2[['State Code','male-percentage-2','female-percentage-2','p-value']]
df4 = df4.rename(columns= {'State Code':'state-code','male-percentage-2':'male-percentage','female-percentage-2':'female-percentage'})
df4.to_csv('../Output/gender-india-b.csv',index =False)

df5 = df2[['State Code','male-percentage-1','female-percentage-1','p-value']]
df5 = df5.rename(columns= {'State Code':'state-code','male-percentage-1':'male-percentage','female-percentage-1':'female-percentage'})
df5.to_csv('../Output/gender-india-a.csv',index =False)
