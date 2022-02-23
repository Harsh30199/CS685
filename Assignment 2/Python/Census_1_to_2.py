#!/usr/bin/env python
# coding: utf-8




import pandas as pd
import numpy as np





df = pd.read_csv('../Datasets Original/Census1.csv')

df = df.groupby('State_Code').sum()
df.reset_index(inplace=True)
df.drop('Sr No',axis='columns',inplace=True)
df.head()





df1 = pd.read_csv('../Dataset/TEMP_STATECODE.csv')
df2 = df.merge(df1,on='State_Code')
df2.drop('State_Code',axis='columns',inplace=True)

df2 = df2[['State Code','State Name','TOT_P','TOT_M','TOT_F']]


df2.head()





totp = df['TOT_P'].sum()
totm = df['TOT_M'].sum()
totf = df['TOT_F'].sum()

df2 = df2.append({'State Code' : 0 ,'State Name' : 'INDIA' , 'TOT_P' : totp , 'TOT_M' : totm , 'TOT_F': totf},ignore_index= True)

df2 = df2.sort_values(by=['State Code'])

df2.to_csv("../Dataset/Census2.csv",index = False)


# In[ ]:




