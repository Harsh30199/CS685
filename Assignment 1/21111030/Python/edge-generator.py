import json
import pandas as pd
import csv
from collections import OrderedDict

import warnings
warnings.filterwarnings("ignore")

data = json.load(open('../Dataset/neighbor-districts-modified.json'))

sortedout = OrderedDict(sorted(data.items())) ##Sorts the dictionary on key

##Sorts the values of list in ascending order
for k ,v in sortedout.items():
    v.sort()
    sortedout[k] = v

edges = []

for k , val in sortedout.items():

    for v in val:
        if [k,v] not in edges and [v,k] not in edges:
            edges.append([k,v])

fields = ['i' , 'j']

with open('../Output/edge-graph.csv', 'w' , newline='') as f:
      
    write = csv.writer(f)
      
    write.writerow(fields)
    write.writerows(edges)
    



