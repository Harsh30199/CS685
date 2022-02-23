
import datetime as dt 
import pandas as pd
import numpy as np
data = pd.read_csv('../cowin_vaccine_data_districtwisemod.csv')

data1 = pd.DataFrame()
sm ={}
dist1 = data['District_Key'].unique()

for i in dist1:

    x = dt.datetime.strptime('2021/01/16','%Y/%m/%d').date()
    y = dt.datetime.strptime('2021/08/14','%Y/%m/%d').date()

    sm['State_Code'] = data[data['District_Key']==i]['State_Code'].iloc[0]
    sm['State'] = data[data['District_Key']==i]['State'].iloc[0]
    sm['Cowin Key'] = data[data['District_Key']==i]['Cowin Key'].iloc[0]
    sm['District_Key'] = data[data['District_Key']==i]['District_Key'].iloc[0]
    sm['District'] = data[data['District_Key']==i]['District'].iloc[0]

    while(x<=y):
      sm['Date']= str(x)
      sm['First_Dose'] = data[data['District_Key']==i][dt.datetime.strftime(x,'%d/%m/%Y')+'.3'].iloc[0]
      sm['Second_Dose'] = data[data['District_Key']==i][dt.datetime.strftime(x,'%d/%m/%Y')+'.4'].iloc[0]
      sm['Male_Vaccinated'] = data[data['District_Key']==i][dt.datetime.strftime(x,'%d/%m/%Y')+'.5'].iloc[0]
      sm['Female_Vaccinated'] = data[data['District_Key']==i][dt.datetime.strftime(x,'%d/%m/%Y')+'.6'].iloc[0]
      sm['Covaxin'] = data[data['District_Key']==i][dt.datetime.strftime(x,'%d/%m/%Y')+'.8'].iloc[0]
      sm['CoviShield'] = data[data['District_Key']==i][dt.datetime.strftime(x,'%d/%m/%Y')+'.9'].iloc[0]

      data1 = data1.append(sm,ignore_index=True)
      x = x + dt.timedelta(days=1)

data1.to_csv('vaccine.csv')
print(data1.head())
  


    





