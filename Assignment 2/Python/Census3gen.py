#!/usr/bin/env python
# coding: utf-8




import pandas as pd
import numpy as np


df = pd.read_excel('../Datasets Original/DDW-C08-0000.xlsx',sheet_name = 'C-08', header = 6 , usecols = [1,3,4,5,6,7,8])
df.columns = ['State Code','State Name','TRU','Age Group','TOT_P','TOT_M','TOT_F']

df = df[df['Age Group'] == 'All ages']
df.drop('Age Group', axis ='columns' , inplace = True)

df.to_csv('../Dataset/Census3.csv',index = False)
