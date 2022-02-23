import pandas as pd
import datetime
import numpy as np

import warnings
warnings.filterwarnings("ignore")

df=pd.read_csv("../Dataset/districts_2.csv")

deldistrict = ['AS_Dibrugarh','AS_Udalguri','MN_Churachandpur']

for d in deldistrict:
    index = df[df['District_Key'] == d].index

    df.drop(index,inplace=True)


calendar=pd.read_csv("../Dataset/Calendar.csv")

df['Date']=pd.to_datetime(df['Date'])
calendar['Date']=pd.to_datetime(calendar['Date'])

df1=df.merge(calendar,on="Date",how="right")

df1['Active'] = np.where(df1['Active'] < 0, 0, df1['Active'])

##District Weekly



df2=df1.groupby(['District_Key','weekid']).sum('Active')

df2.reset_index(inplace=True)

df3=df2[['District_Key','weekid','Active']]

df3=df3.rename(columns={'District_Key':'districtid','weekid':'weekid','Active':'cases'})

df3.to_csv('../Output/cases-week.csv',index=False)


##District Monthly



df4=df1.groupby(['District_Key','monthid']).sum('Active')

df4.reset_index(inplace=True)

df5=df4[['District_Key','monthid','Active']]

df5=df5.rename(columns={'District_Key':'districtid','monthid':'monthid','Active':'cases'})

df5.to_csv('../Output/cases-month.csv',index=False)


##District Overall



df6=df1.groupby(['District_Key']).sum('Active')

df6.reset_index(inplace=True)

df7=df6[['District_Key','Active']]

df7=df7.rename(columns={'District_Key':'districtid','Active':'cases'})

df7.to_csv('../Output/cases-overall.csv',index=False)






