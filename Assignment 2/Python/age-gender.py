#!/usr/bin/env python
# coding: utf-8




import pandas as pd
import numpy as np





df = pd.read_csv('../Dataset/Agewise Census.csv')

df.head(50)





df1 = pd.read_csv('../Dataset/Bi and Tri Age2.csv', usecols=['State Code' , 'State Name','Type' , 'Age Group' , 'Three Male' ,'Three Female'])

df1=df1[df1['Type'] == 'Total']
df1 = df1[df1['Age Group'] != 'Total']
df1 = df1[df1['Age Group'] != 'Age not stated']
df1.head(25)





df2 = df.merge(df1,on=['State Code' , 'Age Group'],how='inner')

df2['male_ratio'] = np.round((df2['Three Male'] / df2['TOT_M']),4)
df2['female_ratio'] = np.round((df2['Three Female'] / df2['TOT_F']),4)

df2.head(50)





data ={}
df4 = pd.DataFrame()

for i in range(36):
    
    df3 = df2[df2['State Code'] == i]
    
    data['state/ut'] = i
    v1 = df3.iloc[df3.male_ratio.argmax(),0:].to_numpy().tolist()
    v2 = df3.iloc[df3.female_ratio.argmax(),0:].to_numpy().tolist()
    
    data['ratio-males'] = v1[10]
    data['age-group-males'] = v1[2]
    data['ratio-females'] = v2[11]
    data['age-group-females'] = v2[2]
    
    df4 =df4.append(data,ignore_index = True)
    
df4.head(50)
df4 = df4[['state/ut','age-group-males','ratio-males','age-group-females','ratio-females']]
df4.to_csv('../Output/age-gender-a.csv',index = False) 





df5 = pd.read_csv('../Dataset/Bi and Tri Age2.csv', usecols=['State Code' , 'State Name' ,'Type', 'Age Group' , 'Two Male' ,'Two Female'])

df5=df5[df5['Type']=='Total']
df5 = df5[df5['Age Group'] != 'Total']
df5 = df5[df5['Age Group'] != 'Age not stated']
df5.head()





df6 = df.merge(df5,on=['State Code' , 'Age Group'],how='inner')

df6['male_ratio'] = np.round((df6['Two Male'] / df6['TOT_M']),4)
df6['female_ratio'] = np.round((df6['Two Female'] / df6['TOT_F']),4)

df6.head(50)





data ={}
df8 = pd.DataFrame()

for i in range(36):
    
    df7 = df6[df6['State Code'] == i]
    
    data['state/ut'] = i
    v1 = df7.iloc[df7.male_ratio.argmax(),0:].to_numpy().tolist()
    v2 = df7.iloc[df7.female_ratio.argmax(),0:].to_numpy().tolist()
    
    data['ratio-males'] = v1[10]
    data['age-group-males'] = v1[2]
    data['ratio-females'] = v2[11]
    data['age-group-females'] = v2[2]
    
    df8 =df8.append(data,ignore_index = True)
    
df8.head(50)
df8 = df8[['state/ut','age-group-males','ratio-males','age-group-females','ratio-females']]
df8.to_csv('../Output/age-gender-b.csv',index = False)





df9 = pd.read_csv('../Dataset/Bi and Tri Age2.csv', usecols=['State Code' , 'State Name','Type' , 'Age Group' , 'Two Male' ,'Two Female' , 'Three Male' , 'Three Female'])

df9 =df9[df9['Type']=='Total']
df9 = df9[df9['Age Group'] != 'Total']
df9 = df9[df9['Age Group'] != 'Age not stated']
df9.head()





df10 = df.merge(df9,on=['State Code' , 'Age Group'],how='inner')


df10['One Male'] = df10['TOT_M'] - df10['Two Male'] - df10['Three Male']
df10['One Female'] = df10['TOT_F'] - df10['Two Female'] - df10['Three Female']


df10['male_ratio'] = np.round((df10['One Male'] / df10['TOT_M']),4)
df10['female_ratio'] = np.round((df10['One Female'] / df10['TOT_F']),4)

df10.head(50)





data ={}
df12 = pd.DataFrame()

for i in range(36):
    
    df11 = df10[df10['State Code'] == i]
    
    data['state/ut'] = i
    v1 = df11.iloc[df11.male_ratio.argmax(),0:].to_numpy().tolist()
    v2 = df11.iloc[df11.female_ratio.argmax(),0:].to_numpy().tolist()

    data['ratio-males'] = v1[14]
    data['age-group-males'] = v1[2]
    data['ratio-females'] = v2[15]
    data['age-group-females'] = v2[2]
    
    df12 =df12.append(data,ignore_index = True)
    
df12.head(50)


df12 = df12[['state/ut','age-group-males','ratio-males','age-group-females','ratio-females']]

df12.to_csv('../Output/age-gender-c.csv',index = False)

