#!/usr/bin/env python
# coding: utf-8




import pandas as pd
import numpy as np





df = pd.read_csv('../Dataset/Census2.csv')

df1 = pd.read_csv('../Dataset/Mono Gender.csv')

df2 = pd.read_csv('../Dataset/Bi and Tri Age2.csv')





data ={}
df3 = pd.DataFrame()
for i in df['State Code'] :
    data['state-code'] = i 
    
    data['percent-one'] = np.round((df1[df1['State Code']== i]['One Total'].iloc[0] / df[df['State Code'] == i]['TOT_P'].iloc[0])*100,4)
    data['percent-two'] = np.round((df2[df2['State Code']== i]['Two Total'].iloc[0] / df[df['State Code'] == i]['TOT_P'].iloc[0])*100,4)
    data['percent-three'] = np.round((df2[df2['State Code']== i]['Three Total'].iloc[0] / df[df['State Code'] == i]['TOT_P'].iloc[0])*100,4)

    df3 = df3.append(data,ignore_index=True)

df3 = df3[['state-code', 'percent-one' , 'percent-two' , 'percent-three']]
df3.to_csv('../Output/percent-india.csv',index=False)

