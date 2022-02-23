#!/usr/bin/env python
# coding: utf-8




import pandas as pd
import numpy as np





df = pd.read_csv('../Dataset/Bi and Tri Age.csv')

df['Two Total'] = df['Two Total'] - df['Three Total']
df['Two Male'] = df['Two Male'] - df['Three Male']
df['Two Female'] = df['Two Female'] - df['Three Female']

df.to_csv('../Dataset/Bi and Tri Age2.csv',index=False)





df = pd.read_csv('../Dataset/Bi and Tri Literacy.csv')

df['Two Total'] = df['Two Total'] - df['Three Total']
df['Two Male'] = df['Two Male'] - df['Three Male']
df['Two Female'] = df['Two Female'] - df['Three Female']

df.to_csv('../Dataset/Bi and Tri Literacy2.csv',index=False)


# In[ ]:




