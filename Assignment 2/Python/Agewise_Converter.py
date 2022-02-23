#!/usr/bin/env python
# coding: utf-8




import pandas as pd
import numpy as np





df = pd.read_csv('../Datasets Original/DDW-0000C-14.csv')
df.head(20)





data ={}
data1={}
df2 = pd.DataFrame()
for i in range(36):
    data ={}
    data1={'TOT_P' : 0 , 'TOT_M' : 0 , 'TOT_F' : 0}
    data2={'TOT_P' : 0 , 'TOT_M' : 0 , 'TOT_F' : 0}
    data3={'TOT_P' : 0 , 'TOT_M' : 0 , 'TOT_F' : 0}
    
    df1 = df[df['State Code'] == i]
    data['State Code'] = i
    if(i==0):
        data['State Name'] = df1['State Name'].iloc[0]
    elif(i==7):
        data['State Name'] = 'Delhi'
    else:
        data['State Name'] = df1['State Name'].iloc[0][0:-5]
    
    for a in df1['Age Group']:
   
        if(a in ['5-9','10-14','15-19','20-24','25-29','Age not stated']):
            data['Age Group'] = a
            data['TOT_P' ] = df1[df1['Age Group'] == a]['TOT_P'].iloc[0]
            data['TOT_M' ] = df1[df1['Age Group' ]== a]['TOT_M'].iloc[0]
            data['TOT_F' ] = df1[df1['Age Group' ]== a]['TOT_F'].iloc[0]
            df2 = df2.append(data,ignore_index = True)
        
        elif(a in ['All ages']):
            data['Age Group'] = 'Total'
            data['TOT_P' ] = df1[df1['Age Group'] == a]['TOT_P'].iloc[0]
            data['TOT_M' ] = df1[df1['Age Group' ]== a]['TOT_M'].iloc[0]
            data['TOT_F' ] = df1[df1['Age Group' ]== a]['TOT_F'].iloc[0]
            df2 = df2.append(data,ignore_index = True)
            
        elif(a in ['30-34','35-39','40-44','45-49']):
            data1['State Code'] = i
            if(i==0):
                data1['State Name'] = df1['State Name'].iloc[0]
            elif(i==7):
                data1['State Name'] = 'Delhi'
            else:
                data1['State Name'] = df1['State Name'].iloc[0][0:-5]
            data1['Age Group'] = '30-49'
            data1['TOT_P' ] += df1[df1['Age Group'] == a]['TOT_P'].iloc[0]
            data1['TOT_M' ] += df1[df1['Age Group' ]== a]['TOT_M'].iloc[0]
            data1['TOT_F' ] += df1[df1['Age Group' ]== a]['TOT_F'].iloc[0]
        
        elif(a in ['50-54','55-59','60-64','65-69']):
            data2['State Code'] = i
            if(i==0):
                data2['State Name'] = df1['State Name'].iloc[0]
            elif(i==7):
                data2['State Name'] = 'Delhi'
            else:
                data2['State Name'] = df1['State Name'].iloc[0][0:-5]
            data2['Age Group'] = '50-69'
            data2['TOT_P' ] += df1[df1['Age Group'] == a]['TOT_P'].iloc[0]
            data2['TOT_M' ] += df1[df1['Age Group' ]== a]['TOT_M'].iloc[0]
            data2['TOT_F' ] += df1[df1['Age Group' ]== a]['TOT_F'].iloc[0]
        
        elif(a in ['70-74','75-79','80+']):
            data3['State Code'] = i
            if(i==0):
                data3['State Name'] = df1['State Name'].iloc[0]
            elif(i==7):
                data3['State Name'] = 'Delhi'
            else:
                data3['State Name'] = df1['State Name'].iloc[0][0:-5]
            data3['Age Group'] = '70+'
            data3['TOT_P' ] += df1[df1['Age Group'] == a]['TOT_P'].iloc[0]
            data3['TOT_M' ] += df1[df1['Age Group' ]== a]['TOT_M'].iloc[0]
            data3['TOT_F' ] += df1[df1['Age Group' ]== a]['TOT_F'].iloc[0]
            
            
    df2 = df2.append(data1,ignore_index = True)
    df2 = df2.append(data2,ignore_index = True)
    df2 = df2.append(data3,ignore_index = True)
    
    
    

df2 = df2[['State Code', 'State Name' , 'Age Group' , 'TOT_P' , 'TOT_M' , 'TOT_F']]

df2.to_csv('../Dataset/Agewise Census.csv' , index = False )
        


# In[ ]:




