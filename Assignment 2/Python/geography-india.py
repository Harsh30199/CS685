#!/usr/bin/env python
# coding: utf-8




import pandas as pd
import numpy as np
from scipy import stats





df = pd.read_csv('../Dataset/Census3.csv')
df1 = df[df['TRU']=='Rural']
df2 = df[df['TRU']=='Urban']


df3 = pd.read_csv('../Dataset/Bi and Tri Age2.csv')
df4 = df3[df3['Type']=='Rural']
df4 = df4[df4['Age Group']=='Total']

df5 = df3[df3['Type']=='Urban']
df5 = df5[df5['Age Group']=='Total']





data ={}
df6 = pd.DataFrame()
for i in df1['State Code'] :
    data['State Code'] = i     
    data['urban-percentage-3'] = np.round((df5[df5['State Code']== i]['Three Total'].iloc[0]/df2[df2['State Code'] == i]['TOT_P'].iloc[0])*100,4)
    data['rural-percentage-3'] = np.round((df4[df4['State Code']== i]['Three Total'].iloc[0] / df1[df1['State Code'] == i]['TOT_P'].iloc[0])*100,4)
    data['urban-percentage-2'] = np.round((df5[df5['State Code']== i]['Two Total'].iloc[0]/df2[df2['State Code'] == i]['TOT_P'].iloc[0])*100,4)
    data['rural-percentage-2'] = np.round((df4[df4['State Code']== i]['Two Total'].iloc[0] / df1[df1['State Code'] == i]['TOT_P'].iloc[0])*100,4)
    data['urban-percentage-1'] = np.round(100-data['urban-percentage-3']-data['urban-percentage-2'],4)
    data['rural-percentage-1'] = np.round(100-data['rural-percentage-3']-data['rural-percentage-2'],4)
    data['urban-to-rural-ratio-2'] = np.round(df5[df5['State Code']== i]['Two Total'].iloc[0]/ df4[df4['State Code']== i]['Two Total'].iloc[0],4)
    data['urban-to-rural-ratio-3'] = np.round(df5[df5['State Code']== i]['Three Total'].iloc[0]/ df4[df4['State Code']== i]['Three Total'].iloc[0],4)
    data['urban-to-rural-ratio-1'] = np.round((data['urban-percentage-1']*df2[df2['State Code'] == i]['TOT_P'].iloc[0])/ (data['rural-percentage-1']*df1[df1['State Code'] == i]['TOT_P'].iloc[0]),4)
    data['urban-to-rural-ratio'] = np.round((df2[df2['State Code'] == i]['TOT_P'].iloc[0]) / (df1[df1['State Code'] == i]['TOT_P'].iloc[0]),4)
    data['t-test'],data['p-value'] = stats.ttest_1samp([data['urban-to-rural-ratio-3'],data['urban-to-rural-ratio-2'],data['urban-to-rural-ratio-1']],data['urban-to-rural-ratio'])
    data['p-value'] = np.round(data['p-value'],4)
    df6 = df6.append(data,ignore_index=True)

df6.head(25)





df7 = df6[['State Code','urban-percentage-3','rural-percentage-3','p-value']]
df7 = df7.rename(columns= {'State Code':'state-code','urban-percentage-3':'urban-percentage','rural-percentage-3':'rural-percentage'})
df7.to_csv('../Output/geography-india-c.csv',index =False)


df8 = df6[['State Code','urban-percentage-2','rural-percentage-2','p-value']]
df8 = df8.rename(columns= {'State Code':'state-code','urban-percentage-2':'urban-percentage','rural-percentage-2':'rural-percentage'})
df8.to_csv('../Output/geography-india-b.csv',index =False)

df9 = df6[['State Code','urban-percentage-1','rural-percentage-1','p-value']]
df9 = df9.rename(columns= {'State Code':'state-code','urban-percentage-1':'urban-percentage','rural-percentage-1':'rural-percentage'})
df9.to_csv('../Output/geography-india-a.csv',index =False)

