

import numpy as np
import pandas as pd
import sys
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from imblearn.over_sampling import SMOTE



df = pd.read_csv('training-s145.csv',header=None)

for i in range (1,11):
    df[i] = pd.to_numeric(df[i])

duplicate = df[df.duplicated()] ##Checks if Duplicate Rows present

if(len(duplicate)!=0):
    df.drop_duplicates(inplace = True) ## If duplicate rows are found then they are dropped

uniq,uniqcount = np.unique(np.array(df[0]),return_counts=True)

X = df.loc[:,1:11]
Y= df.loc[:,0]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.148)

neigh = KNeighborsClassifier(n_neighbors=5,weights='distance')
neigh.fit(X_train, Y_train)



sm = SMOTE()
X_res, Y_res = sm.fit_resample(X, Y)

uniq,uniqcount = np.unique(np.array(Y_res),return_counts=True)

Xsmot_train, Xsmot_test, Ysmot_train, Ysmot_test = train_test_split(X_res, Y_res, test_size=0.242)

neighsmot = KNeighborsClassifier(n_neighbors=5,weights='distance')
neighsmot.fit(Xsmot_train, Ysmot_train)
neighsmot.score(Xsmot_test, Ysmot_test)*100

neighsmot2 = KNeighborsClassifier()
param_grid = {'n_neighbors': np.arange(1,20),'weights':['distance','uniform'],'p': np.arange(1,5)}
knn_gscv = GridSearchCV(neighsmot2, param_grid, cv=5)
knn_gscv.fit(X_res, Y_res)


best_k = knn_gscv.best_params_['n_neighbors']
best_distance = knn_gscv.best_params_['weights']
best_p = knn_gscv.best_params_['p']

bestneigh = KNeighborsClassifier(n_neighbors=best_k,weights=best_distance, p = best_p)
bestneigh.fit(X_res, Y_res)
test_data = pd.read_csv(sys.argv[1],header=None)
X_test = test_data.loc[:,1:11]
Y_test = test_data.loc[:,0]

y_pred = bestneigh.predict(X_test)
print(neighsmot.score(X_test, Y_test)*100)
output =pd.DataFrame(y_pred)
output.to_csv('answer-s145.csv',index=False,header=None)
