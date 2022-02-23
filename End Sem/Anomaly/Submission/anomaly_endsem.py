
import numpy as np
import pandas as pd

from sklearn.neighbors import LocalOutlierFactor


df = pd.read_csv('anomaly-s145.dat',header=None,delimiter='\t')

df.dropna(inplace=True,axis='columns')


data = df.values
data =data.flatten()


lof = LocalOutlierFactor(n_neighbors=5)
y_pred = lof.fit_predict(data.reshape(-1,1))

y_pred = np.where(y_pred == 1 , 0 ,y_pred)
y_pred = np.where(y_pred == -1 , 1 ,y_pred)
y_pred = y_pred.reshape(100,100)
mask=[]
for i in range(100):
    s = ''
    
    for j in y_pred[i]:
        s+= str(1) if j ==1 else str(0)
        s+= ' '
    mask.append(s)

file = open('answer-s145.dat','w')

for m in mask:
    file.write(m + '\n')



