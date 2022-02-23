#!/usr/bin/env python
# coding: utf-8




import pandas as pd
import numpy as np





df = pd.read_csv('../Dataset/Bi and Tri Age2.csv')
df = df[df['Type'] == 'Total']
df = df[df['Age Group'] == 'Total']

df1 = pd.read_csv('../Dataset/Mono Gender.csv')
df1.head()

df = df.merge(df1,on = 'State Code', how = 'inner')
df.head(36)





df['2-to-1-ratio'] = np.round(df['Two Total'] / df['One Total'],4)

df2 = df.sort_values('2-to-1-ratio', ignore_index = True , ascending = False)[0:3]

df3 = df.sort_values('2-to-1-ratio', ignore_index = True , ascending = True)[0:3]

df2 = df2.append(df3)

df2.drop(['State Name_x','State Name_y','One Total','One Male','One Female','Type','Age Group','Two Total','Two Male','Two Female' , 'Three Total' , 'Three Male' , 'Three Female'], axis = 'columns' , inplace = True)
df2 = df2.rename(columns={'State Code':'state-code'})
df2.to_csv('../Output/2-to-1-ratio.csv',index = False)

