#!/usr/bin/env python
# coding: utf-8




import pandas as pd
import numpy as np





df = pd.DataFrame()
cols = {'1':'State Code','2':'State Name','4':'Language','5':'Total'}


for i in range(0,10):
    temp1 = pd.read_excel('../Datasets Original/C17/DDW-C17-0'+str(i)+'00.XLSX',sheet_name = 'Sheet1', header = 4 , usecols = [0,1,3,4] )
    temp1.rename(columns = {i : str(i) for i in [1,2,4,5]},inplace=True)
    temp1.dropna(axis='rows',inplace=True)
    
    temp2 = pd.read_excel('../Datasets Original/C17/DDW-C17-0'+str(i)+'00.XLSX',sheet_name = 'Sheet1', header = 4 , usecols = [0,1,8,9] )
    temp2.rename(columns = {i : str(i) for i in [1,2]},inplace=True)
    temp2.rename(columns = {i : str(int(i)-5) for i in [9,10,'9','10']},inplace=True)
    
    temp2.dropna(axis='rows',inplace=True)
    
    temp3 = pd.read_excel('../Datasets Original/C17/DDW-C17-0'+str(i)+'00.XLSX',sheet_name = 'Sheet1', header = 4 , usecols = [0,1,13,14] )
    temp3.rename(columns = {i : str(i) for i in [1,2]},inplace=True)
    temp3.rename(columns = {i : str(int(i)-10) for i in [14,15,'14','15']},inplace=True)
   
    temp3.dropna(axis='rows',inplace=True)
    
    df = pd.concat([df,temp1,temp2,temp3],ignore_index=True)

for i in range(10,36):
    temp1 = pd.read_excel('../Datasets Original/C17/DDW-C17-'+str(i)+'00.XLSX',sheet_name = 'Sheet1', header = 4 , usecols = [0,1,3,4] )
    temp1.rename(columns = {i : str(i) for i in [1,2,4,5]},inplace=True)
    temp1.dropna(axis='rows',inplace=True)
    
    temp2 = pd.read_excel('../Datasets Original/C17/DDW-C17-'+str(i)+'00.XLSX',sheet_name = 'Sheet1', header = 4 , usecols = [0,1,8,9] )
    temp2.rename(columns = {i : str(i) for i in [1,2]},inplace=True)
    temp2.rename(columns = {i : str(int(i)-5) for i in ['9','10',9,10]},inplace=True)
   
    temp2.dropna(axis='rows',inplace=True)
    
    temp3 = pd.read_excel('../Datasets Original/C17/DDW-C17-'+str(i)+'00.XLSX',sheet_name = 'Sheet1', header = 4 , usecols = [0,1,13,14] )
    temp3.rename(columns = {i : str(i) for i in [1,2]},inplace=True)
    temp3.rename(columns = {i : str(int(i)-10) for i in [14,15,'14','15']},inplace=True)
    
    temp3.dropna(axis='rows',inplace=True)
    
    df = pd.concat([df,temp1,temp2,temp3],ignore_index=True)
df.rename(columns = cols,inplace=True)





df.to_csv('../Dataset/Language Total Speakers Statewise.csv',index=False)

