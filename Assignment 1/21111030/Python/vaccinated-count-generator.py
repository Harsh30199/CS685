
import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings("ignore")

df=pd.read_csv("../Dataset/vaccine.csv")


df['Date']=df.Date.astype('datetime64[ns]')


calendar=pd.read_csv("../Dataset/Calendar2.csv")



calendar['Date']=calendar.Date.astype('datetime64[ns]')


df1=df.merge(calendar,on="Date",how="right")

df1['First Dose'] = np.where(df1['First Dose'] < 0, 0, df1['First Dose'])
df1['Second Dose'] = np.where(df1['Second Dose'] < 0, 0, df1['Second Dose'])

## District Weekly


df2=df1.groupby(['District_Key','weekid']).sum(['First Dose','Second Dose'])

df2.reset_index(inplace=True)


df3=df2[['District_Key','weekid','First Dose','Second Dose']]



df3.sort_values(by=['District_Key','weekid'], inplace=True)


df3=df3.rename(columns={'District_Key':'districtid','weekid':'weekid','First Dose':'dose1','Second Dose':'dose2'})

df3.to_csv('../Output/district-vaccinated-count-week.csv',index=False)


## District Monthly



df4=df1.groupby(['District_Key','monthid']).sum(['First Dose','Second Dose'])

df4.reset_index(inplace=True)


df5=df4[['District_Key','monthid','First Dose','Second Dose']]



df5.sort_values(by=['District_Key','monthid'], inplace=True)


df5=df5.rename(columns={'District_Key':'districtid','monthid':'monthid','First Dose':'dose1','Second Dose':'dose2'})

df5.to_csv('../Output/district-vaccinated-count-month.csv',index=False)

## District Overall



df6=df1.groupby(['District_Key']).sum(['First Dose','Second Dose'])

df6.reset_index(inplace=True)


df7=df6[['District_Key','First Dose','Second Dose']]



df7.sort_values(by=['District_Key'], inplace=True)


df7=df7.rename(columns={'District_Key':'districtid','First Dose':'dose1','Second Dose':'dose2'})

df7.to_csv('../Output/district-vaccinated-count-overall.csv',index=False)


##States Weekly



df8 = df1.groupby(['State_Code','weekid']).sum(['First Dose','Second Dose'])

df8.reset_index(inplace=True)

df9=df8[['State_Code','weekid','First Dose','Second Dose']]

df9.sort_values(by=['State_Code','weekid'], inplace=True)

df9=df9.rename(columns={'State_Code':'stateid','weekid':'weekid','First Dose':'dose1','Second Dose':'dose2'})

df9.to_csv('../Output/state-vaccinated-count-week.csv',index=False)



##States Monthly


df10 = df1.groupby(['State_Code','monthid']).sum(['First Dose','Second Dose'])

df10.reset_index(inplace=True)

df11=df10[['State_Code','monthid','First Dose','Second Dose']]

df11.sort_values(by=['State_Code','monthid'], inplace=True)

df11=df11.rename(columns={'State_Code':'stateid','monthid':'monthid','First Dose':'dose1','Second Dose':'dose2'})

df11.to_csv('../Output/state-vaccinated-count-month.csv',index=False)


##States Overall

df12 = df1.groupby(['State_Code']).sum(['First Dose','Second Dose'])

df12.reset_index(inplace=True)

df13=df12[['State_Code','First Dose','Second Dose']]

df13.sort_values(by=['State_Code'], inplace=True)

df13=df13.rename(columns={'State_Code':'stateid','First Dose':'dose1','Second Dose':'dose2'})

df13.to_csv('../Output/state-vaccinated-count-overall.csv',index=False)


