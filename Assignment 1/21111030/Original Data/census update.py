import pandas as pd
import numpy as np
data = pd.read_csv('../Census_og.csv')
disdiff = pd.read_csv('../difference district.csv')

data1 = pd.DataFrame()
sm ={}

w = disdiff['neighbor json'].unique()

c = disdiff['districtwise'].unique()
dict1 = {w[x].lstrip():c[x].lstrip() for x in range(len(w))}

##keys = list(dict1.keys())

  
for idx , row in data.iterrows():
    sm['TOT_P'] = data[data['Name']==row['Name']]['TOT_P'].iloc[0]
    sm['TOT_M'] = data[data['Name']==row['Name']]['TOT_M'].iloc[0]
    sm['TOT_F'] = data[data['Name']==row['Name']]['TOT_F'].iloc[0]
  
    if(row['Name'] in dict1.keys()):
        ##print(row['Name'])
        sm['Name'] = dict1[row['Name']]

    else:
        sm['Name'] = data[data['Name']==row['Name']]['Name'].iloc[0]

    ##print(sm)
    data1 = data1.append(sm,ignore_index=True)

    

data1.to_csv('census_mod.csv')

