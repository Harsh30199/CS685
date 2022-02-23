
import pandas as pd
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

df1['Date']=pd.to_datetime(df1['Date'])


df1['Year']=df1.Date.dt.to_period('Y')



wave1=df1[df1['Year']=='2020']
wave2=df1[df1['Year']=='2021']



###District 

districts=wave1['District_Key'].unique()



wave1_final = pd.DataFrame(columns = ['districtid', 'wave1-weekid', 'wave1-monthid'])
df2 = wave1.groupby(['District_Key','weekid']).sum('Active')
df2.reset_index(inplace=True)
df2 = df2[['District_Key','weekid','Active']]
df3 = wave1.groupby(['District_Key','weekid2']).sum('Active')
df3.reset_index(inplace=True)
df3 = df3[['District_Key','weekid2','Active']]
df4 = wave1.groupby(['District_Key','monthid']).sum('Active')
df4.reset_index(inplace=True)
df4 = df4[['District_Key','monthid','Active']]

for i in districts:
    data1=df2[df2['District_Key']==i]
    data2=df3[df3['District_Key']==i]
    v1=data1.iloc[data1.Active.argmax(),0:3].to_numpy().tolist()
    v2=data2.iloc[data2.Active.argmax(),0:3].to_numpy().tolist()
    if(v1[2]>v2[2]):
        weekid=(v1[1]*2)-1
    else:
        weekid=(v2[1]*2)
    
    data3=df4[df4['District_Key']==i]
    v3=data3.iloc[data3.Active.argmax(),0:3].to_numpy().tolist()
    monthid=v3[1]
    
    wave1_final = wave1_final.append({'districtid' : i, 'wave1-weekid' : weekid, 'wave1-monthid' : monthid}, 
                ignore_index = True)
    del data1
    del data2
    del data3
    
   

  
    

districts2=wave2['District_Key'].unique()


wave2_final = pd.DataFrame(columns = ['districtid', 'wave2-weekid', 'wave2-monthid'])
df2 = wave2.groupby(['District_Key','weekid']).sum('Active')
df2.reset_index(inplace=True)
df2 = df2[['District_Key','weekid','Active']]
df3 = wave2.groupby(['District_Key','weekid2']).sum('Active')
df3.reset_index(inplace=True)
df3 = df3[['District_Key','weekid2','Active']]
df4 = wave2.groupby(['District_Key','monthid']).sum('Active')
df4.reset_index(inplace=True)
df4 = df4[['District_Key','monthid','Active']]


for i in districts2:
    data1=df2[df2['District_Key']==i]
    data2=df3[df3['District_Key']==i]
    v1=data1.iloc[data1.Active.argmax(),0:3].to_numpy().tolist()
    v2=data2.iloc[data2.Active.argmax(),0:3].to_numpy().tolist()
    if(v1[2]>v2[2]):
        weekid=(v1[1]*2)-1
    else:
        weekid=(v2[1]*2)
    
    data3=df4[df4['District_Key']==i]
    v3=data3.iloc[data3.Active.argmax(),0:3].to_numpy().tolist()
    monthid=v3[1]
    
    wave2_final = wave2_final.append({'districtid' : i, 'wave2-weekid' : weekid, 'wave2-monthid' : monthid}, 
                ignore_index = True)
    del data1
    del data2
    del data3



wave=wave1_final.merge(wave2_final,on="districtid",how='outer')

wave.sort_values('districtid',inplace=True,ignore_index=True)

wave = wave[['districtid','wave1-weekid','wave2-weekid','wave1-monthid','wave2-monthid']]

wave.to_csv('../Output/district-peaks.csv',index=False)


###State


states=wave1['State_Code'].unique()


wave1_final_s = pd.DataFrame(columns = ['stateid', 'wave1-weekid', 'wave1-monthid'])

df5 = wave1.groupby(['State_Code','weekid']).sum('Active')
df5.reset_index(inplace=True)
df5 = df5[['State_Code','weekid','Active']]
df6 = wave1.groupby(['State_Code','weekid2']).sum('Active')
df6.reset_index(inplace=True)
df6 = df6[['State_Code','weekid2','Active']]
df7 = wave1.groupby(['State_Code','monthid']).sum('Active')
df7.reset_index(inplace=True)
df7 = df7[['State_Code','monthid','Active']]

for i in states:
    data1=df5[df5['State_Code']==i]
    data2=df6[df6['State_Code']==i]
    v1=data1.iloc[data1.Active.argmax(),0:3].to_numpy().tolist()
    v2=data2.iloc[data2.Active.argmax(),0:3].to_numpy().tolist()
    if(v1[2]>v2[2]):
        weekid=(v1[1]*2)-1
    else:
        weekid=(v2[1]*2)
    
    data3=df7[df7['State_Code']==i]
    v3=data3.iloc[data3.Active.argmax(),0:3].to_numpy().tolist()
    monthid=v3[1]
    
    wave1_final_s = wave1_final_s.append({'stateid' : i, 'wave1-weekid' : weekid, 'wave1-monthid' : monthid}, 
                ignore_index = True)
    del data1
    del data2
    del data3


states=wave2['State_Code'].unique()

wave2_final_s = pd.DataFrame(columns = ['stateid', 'wave2-weekid', 'wave2-monthid'])

df5 = wave2.groupby(['State_Code','weekid']).sum('Active')
df5.reset_index(inplace=True)
df5 = df5[['State_Code','weekid','Active']]
df6 = wave2.groupby(['State_Code','weekid2']).sum('Active')
df6.reset_index(inplace=True)
df6 = df6[['State_Code','weekid2','Active']]
df7 = wave2.groupby(['State_Code','monthid']).sum('Active')
df7.reset_index(inplace=True)
df7 = df7[['State_Code','monthid','Active']]

for i in states:
    data1=df5[df5['State_Code']==i]
    data2=df6[df6['State_Code']==i]
    v1=data1.iloc[data1.Active.argmax(),0:3].to_numpy().tolist()
    v2=data2.iloc[data2.Active.argmax(),0:3].to_numpy().tolist()
    if(v1[2]>v2[2]):
        weekid=(v1[1]*2)-1
    else:
        weekid=(v2[1]*2)
    
    data3=df7[df7['State_Code']==i]
    v3=data3.iloc[data3.Active.argmax(),0:3].to_numpy().tolist()
    monthid=v3[1]
    
    wave2_final_s = wave2_final_s.append({'stateid' : i, 'wave2-weekid' : weekid, 'wave2-monthid' : monthid}, 
                ignore_index = True)
    del data1
    del data2
    del data3


wave_s =wave1_final_s.merge(wave2_final_s,on="stateid",how='outer')
wave_s.sort_values('stateid',inplace=True,ignore_index=True)
wave_s = wave_s[['stateid','wave1-weekid','wave2-weekid','wave1-monthid','wave2-monthid']]
wave_s.to_csv('../Output/state-peaks.csv',index=False)



###Overall

df8=wave1.groupby('weekid').sum('Active')
df8.reset_index(inplace=True)
df8 = df8[['weekid','Active']]
df9=wave1.groupby('weekid2').sum('Active')
df9.reset_index(inplace=True)
df9 = df9[['weekid2','Active']]
df10=wave1.groupby('monthid').sum('Active')
df10.reset_index(inplace=True)
df10 = df10[['monthid','Active']]

wave1_final_o = pd.DataFrame(columns = ['wave1-weekid', 'wave1-monthid'])
v1=df8.iloc[df8.Active.argmax(),0:2].to_numpy().tolist()
v2=df9.iloc[df9.Active.argmax(),0:2].to_numpy().tolist()
v3=df10.iloc[df10.Active.argmax(),0:2].to_numpy().tolist()
if(v1[1]>v2[1]):
    weekid=(v1[0]*2)-1
else:
    weekid=(v2[0]*2)

monthid=v3[0]
wave1_final_o = wave1_final_o.append({ 'wave1-weekid' : weekid, 'wave1-monthid' : monthid}, 
                ignore_index = True)


df8=wave2.groupby('weekid').sum('Active')
df8.reset_index(inplace=True)
df8 = df8[['weekid','Active']]
df9=wave2.groupby('weekid2').sum('Active')
df9.reset_index(inplace=True)
df9 = df9[['weekid2','Active']]
df10=wave2.groupby('monthid').sum('Active')
df10.reset_index(inplace=True)
df10 = df10[['monthid','Active']]

wave2_final_o = pd.DataFrame(columns = ['wave2-weekid', 'wave2-monthid'])
v1=df8.iloc[df8.Active.argmax(),0:2].to_numpy().tolist()
v2=df9.iloc[df9.Active.argmax(),0:2].to_numpy().tolist()
v3=df10.iloc[df10.Active.argmax(),0:2].to_numpy().tolist()
if(v1[1]>v2[1]):
    weekid=(v1[0]*2)-1
else:
    weekid=(v2[0]*2)

monthid=v3[0]
wave2_final_o = wave2_final_o.append({ 'wave2-weekid' : weekid, 'wave2-monthid' : monthid}, 
                ignore_index = True)




wave_o=wave1_final_o.join(wave2_final_o)

wave_o['Country']='India'

wave_o = wave_o.reindex(columns=['Country','wave1-weekid','wave2-weekid','wave1-monthid','wave2-monthid'])

wave_o.to_csv('../Output/overall-peaks.csv',index=False)




