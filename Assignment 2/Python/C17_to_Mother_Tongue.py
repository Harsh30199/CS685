#!/usr/bin/env python
# coding: utf-8




import pandas as pd
import numpy as np





df = pd.DataFrame()
cols = {'1':'State Code','2':'State Name','4':'Language','5':'Total'}
for i in range(0,10):
    temp = pd.read_excel('../Datasets Original/C17/DDW-C17-0'+str(i)+'00.XLSX',sheet_name = 'Sheet1', header = 4 , usecols = [0,1,3,4] )
    temp.rename(columns = {i : str(i) for i in [1,2,4,5]},inplace=True)
    temp.dropna(axis='rows',inplace=True)
    df = pd.concat([df,temp],ignore_index=True)

for i in range(10,36):
    temp = pd.read_excel('../Datasets Original/C17/DDW-C17-'+str(i)+'00.XLSX',sheet_name = 'Sheet1', header = 4 , usecols = [0,1,3,4] )
    temp.rename(columns = {i : str(i) for i in [1,2,4,5]},inplace=True)
    temp.dropna(axis='rows',inplace=True)
    df = pd.concat([df,temp],ignore_index=True)

df.rename(columns = cols,inplace=True)





df.to_csv('../Dataset/Mother Tongue Statewise.csv',index=False)

