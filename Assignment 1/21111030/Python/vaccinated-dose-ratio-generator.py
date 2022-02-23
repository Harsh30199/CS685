import numpy as np
import pandas as pd
import csv

import warnings
warnings.filterwarnings("ignore")


census=pd.read_csv("../Dataset/Census1.csv")



df=pd.read_csv("../Dataset/vaccine.csv")


df['First Dose'] = np.where(df['First Dose'] < 0, 0, df['First Dose'])
df['Second Dose'] = np.where(df['Second Dose'] < 0, 0, df['Second Dose'])


df2=df.groupby(["District_Key"]).sum()


df2.reset_index(inplace= True)


df3=df2.merge(census,on="District_Key")


df3['vaccinateddose1ratio']=df3['First Dose']/df3['TOT_P']
df3['vaccinateddose2ratio']=df3['Second Dose']/df3['TOT_P']


df4=df3[['District_Key','vaccinateddose1ratio','vaccinateddose2ratio']]
df4=df4.rename(columns={'District_Key':'districtid','vaccinateddose1ratio':'vaccinateddose1ratio','vaccinateddose2ratio':'vaccinateddose2ratio'})


df4.sort_values(by=['vaccinateddose1ratio'], inplace=True)

df4.to_csv("../Output/district-vaccinated-dose-ratio.csv",index=False)


####State Wise

df5=df.groupby(["State_Code"]).sum()


df5.reset_index(inplace= True)

c=census.groupby(['State_Code']).sum()
c.reset_index(inplace=True)


df6=df5.merge(c,on="State_Code")


df6['vaccinateddose1ratio']=df6['First Dose']/df6['TOT_P']
df6['vaccinateddose2ratio']=df6['Second Dose']/df6['TOT_P']


df7=df6[['State_Code','vaccinateddose1ratio','vaccinateddose2ratio']]
df7=df7.rename(columns={'State_Code':'stateid','vaccinateddose1ratio':'vaccinateddose1ratio','vaccinateddose2ratio':'vaccinateddose2ratio'})


df7.sort_values(by=['vaccinateddose1ratio'], inplace=True)

df7.to_csv("../Output/state-vaccinated-dose-ratio.csv",index=False)


####Overall

dose1 = df['First Dose'].sum()
dose2 = df['Second Dose'].sum()


totalpop = census['TOT_P'].sum()

data={}
data['Country'] = 'India'
data['vaccinateddose1ratio'] = dose1/totalpop
data['vaccinateddose2ratio'] = dose2/totalpop



with open('../Output/overall-vaccinated-dose-ratio.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Country','vaccinateddose1ratio','vaccinateddose2ratio'])
        writer.writeheader()
        writer.writerow(data)


