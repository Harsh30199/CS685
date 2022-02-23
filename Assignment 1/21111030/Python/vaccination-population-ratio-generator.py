import numpy as np
import pandas as pd
import csv

import warnings
warnings.filterwarnings("ignore")

census=pd.read_csv("../Dataset/Census1.csv")


df=pd.read_csv("../Dataset/vaccine.csv")


df['Female vaccinated'] = np.where(df['Female vaccinated'] < 0, 0, df['Female vaccinated'])
df['Male Vaccinated'] = np.where(df['Male Vaccinated'] < 0, 0, df['Male Vaccinated'])

df2=df.groupby(["District_Key"]).sum()


df2.reset_index(inplace= True)



df3=df2.merge(census,on="District_Key")


df3['vaccinationratio']=df3['Female vaccinated']/df3['Male Vaccinated']
df3['populationratio']=df3['TOT_F']/df3['TOT_M']
df3['ratioofratios']=df3['vaccinationratio']/df3['populationratio']

df4=df3[['District_Key','vaccinationratio','populationratio','ratioofratios']]
df4=df4.rename(columns={'District_Key':'districtid','vaccinationratio':'vaccinationratio','populationratio':'populationratio','ratioofratios':'ratioofratios'})


df4.sort_values(by=['ratioofratios'], inplace=True)


df4.to_csv("../Output/district-vaccination-population-ratio.csv",index=False)

#####Statewise


df5=df.groupby(["State_Code"]).sum()
df5.reset_index(inplace= True)

c=census.groupby(['State_Code']).sum()
c.reset_index(inplace=True)

df6=df5.merge(c,on="State_Code")


df6['vaccinationratio']=df6['Female vaccinated']/df6['Male Vaccinated']
df6['populationratio']=df6['TOT_F']/df6['TOT_M']
df6['ratioofratios']=df6['vaccinationratio']/df6['populationratio']

df7=df6[['State_Code','vaccinationratio','populationratio','ratioofratios']]
df7=df7.rename(columns={'State_Code':'stateid','vaccinationratio':'vaccinationratio','populationratio':'populationratio','ratioofratios':'ratioofratios'})

df7.sort_values(by=['ratioofratios'], inplace=True)

df7.to_csv("../Output/state-vaccination-population-ratio.csv",index=False)


#####Overall

femvacc = df['Female vaccinated'].sum()
malevacc = df['Male Vaccinated'].sum()

vaccinationratio = femvacc/malevacc

totalfempop = census['TOT_F'].sum()
totalmalepop = census['TOT_M'].sum()

populationratio = totalfempop/totalmalepop

ratioofratios = vaccinationratio/populationratio

data={}
data['Country'] = 'India'
data['vaccinationratio'] = vaccinationratio
data['populationratio'] = populationratio
data['ratioofratios'] = ratioofratios



with open('../Output/overall-vaccination-population-ratio.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Country','vaccinationratio','populationratio','ratioofratios'])
        writer.writeheader()
        writer.writerow(data)
