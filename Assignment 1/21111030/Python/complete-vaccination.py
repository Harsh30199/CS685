

import pandas as pd
import numpy as np
import datetime

import warnings
warnings.filterwarnings("ignore")

df=pd.read_csv("../Dataset/vaccine.csv")

df['First Dose'] = np.where(df['First Dose'] < 0, 0, df['First Dose'])


total=df.groupby(['State_Code']).sum()

total.reset_index(inplace=True)
total.drop(['Unnamed: 0', 'First_Dose', 'Second_Dose',
       'Second Dose', 'Male_Vaccinated', 'Male Vaccinated',
       'Female_Vaccinated', 'Female vaccinated', 'Covaxin_Vaccinated',
       'Covaxin', 'CoviShield_Vaccinated', 'Covishield'],axis=1,inplace=True)

total=total.rename(columns={'First Dose':'total vaccinated'})



df['Date']=df.Date.astype('datetime64[ns]')




calendar=pd.read_csv("../Dataset/Calendar2.csv")



calendar['Date']=calendar.Date.astype('datetime64[ns]')





df1=df.merge(calendar,on="Date",how="right")





df2=df1[df1['weekid']==31]



df3=df2.groupby(['State_Code']).sum()
df3.reset_index(inplace=True)



census=pd.read_csv("../Dataset/Census1.csv")


c=census.groupby(['State_Code']).sum()
c.reset_index(inplace=True)



df4=df3.merge(c,on="State_Code")


df5=df4.merge(total,on="State_Code")



df5['Rate']=(df5['First Dose']/7).apply(np.ceil)
df5['populationleft']=df5['TOT_P']-df5['total vaccinated']
df5.populationleft = np.where(df5.populationleft < 0, 0, df5.populationleft)
df5['days left']=(df5['populationleft']/df5['Rate']).apply(np.ceil)


df5['days left'] = df5['days left'].replace(np.nan, 0)



initial_date = "8/14/2021"
df5['date of completion']=''
for i in range(0,len(df5)):
    df5.at[i,'date of completion'] = pd.to_datetime(initial_date) + pd.DateOffset(days=df5.at[i,'days left'])
    df5.at[i,'date of completion'] = df5.at[i,'date of completion'].date()








df6=df5[['State_Code','populationleft','Rate','date of completion']]
df6=df6.rename(columns={'State_Code':'stateid','populationleft':'populationleft','Rate':'rateofvaccination','date of completition':'date'})
df6.head()





df6.to_csv('../Output/complete-vaccination.csv',index=False)







