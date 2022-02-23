#!/usr/bin/env python
# coding: utf-8




import pandas as pd
import numpy as np





df = pd.read_csv('../Dataset/Bi and Tri Age2.csv')
df = df[df['Type'] == 'Total']
df = df[df['Age Group'] == 'Total']

df.head()





df['3-to-2-ratio'] = np.round(df['Three Total'] / df['Two Total'],4)

df2 = df.sort_values('3-to-2-ratio', ignore_index = True , ascending = False)[0:3]

df3 = df.sort_values('3-to-2-ratio', ignore_index = True , ascending = True)[0:3]

df2 = df2.append(df3)

df2.drop(['State Name','Type','Age Group','Two Total','Two Male','Two Female' , 'Three Total' , 'Three Male' , 'Three Female'], axis = 'columns' , inplace = True)

df2 = df2.rename(columns={'State Code':'state-code'})
df2.to_csv('../Output/3-to-2-ratio.csv',index = False)

