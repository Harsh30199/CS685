


import json
import pandas as pd
import numpy as np





nd = json.load(open('neighbor-districts.json'))
nd= {i.split("/")[0] : [k.split("/")[0] for k in values] for i,values in nd.items()}
nd= {i.split("_district")[0] : [k.split("_district")[0] for k in values] for i,values in nd.items()}

nd




disdiff = pd.read_csv('difference district.csv')
w = disdiff['neighbor json'].unique()

c = disdiff['districtwise'].unique()
dict1 = {w[x].lstrip():c[x].lstrip() for x in range(len(w))}





dict1
print(type(nd))





nd1={}
for k,val  in nd.items():
    a=''
    b=[]
    if k in dict1.keys():
        a=dict1[k].title()
    else:
        a = k.title()
    for v in val:
        if v in dict1.keys():
            b.append(dict1[v].title())
        else:
            b.append(v.title())
    nd1[a]=b
    
with open("out.json", "w") as outfile:
    json.dump(nd1, outfile)





district_key = pd.read_csv('district_key.csv')
district_key.head(100)
district_key = pd.Series(district_key.District_Key.values,index=district_key.District).to_dict()
district_key





nd2={}
for k,val  in nd1.items():
    a=''
    b=[]
    a = k.replace('_'," ")
    for v in val :
        b.append(v.replace('_'," "))
    nd2[a]=b

print(nd2)






nd3={}

for k,val  in nd2.items():
    a=''
    b=[]
    ##print(k)
    if k in district_key.keys():
        ##print(1)
        a = district_key[k]
        ##print(a)
    else:
        a = k
    for v in val:
        if v in district_key.keys():
            b.append(district_key[v])
        else:
            b.append(v)
    nd3[a]=b
        
with open("out.json", "w") as outfile:
    json.dump(nd3, outfile)

nd3





from collections import OrderedDict
out = json.load(open('Imp Data/neighbor-districts-modified.json'))
sortedout = OrderedDict(sorted(out.items()))

for k ,v in sortedout.items():
    v.sort()
    sortedout[k] = v

with open("Imp Data/neighbor-districts-modified.json", "w") as outfile:
    json.dump(sortedout, outfile)

