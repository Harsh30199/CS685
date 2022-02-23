import numpy as np
import pandas as pd
import csv

import warnings
warnings.filterwarnings("ignore")


df=pd.read_csv("../Dataset/vaccine.csv")

df['Covishield'] = np.where(df['Covishield'] < 0, 0, df['Covishield'])
df['Covaxin'] = np.where(df['Covaxin'] < 0, 0, df['Covaxin'])

df2=df.groupby(['District_Key']).sum(['Covaxin','Covishield'])




df2.reset_index(inplace=True)
df2['vaccineratio']=df2['Covishield']/df2['Covaxin']


df3=df2[['District_Key','vaccineratio']]



df3=df3.rename(columns={'District_Key':'districtid','vaccineratio':'vaccineratio'})



df3.sort_values(by=['vaccineratio'], inplace=True)
df3.head()



df3.to_csv("../Output/district-vaccine-type-ratio.csv",index=False)

###Statewise

df4=df.groupby(['State_Code']).sum(['Covaxin','Covishield'])

df4.reset_index(inplace=True)
df4['vaccineratio']=df4['Covishield']/df4['Covaxin']

df5=df4[['State_Code','vaccineratio']]

df5=df5.rename(columns={'State_Code':'stateid','vaccineratio':'vaccineratio'})

df5.sort_values(by=['vaccineratio'], inplace=True)

df5.to_csv("../Output/state-vaccine-type-ratio.csv",index=False)


#####Overall

covaxin=df['Covaxin'].sum()
covishield=df['Covishield'].sum()
vaccineratio=covishield/covaxin


data={}
data['Country'] = 'India'
data['vaccineratio'] = vaccineratio

with open('../Output/overall-vaccine-type-ratio.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Country','vaccineratio'])
        writer.writeheader()
        writer.writerow(data)


