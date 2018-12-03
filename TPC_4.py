#Fazer imports

from sklearn import datasets, tree, model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

digits = datasets.load_digits()

#Maus Resultados
print("Maus Resultados:")
res = model.predict(features_test)
err_features=features_test[res!=classes_test,:][:2]
print("actual: ",classes_test[res!=classes_test])
print("predict:",res[res!=classes_test])

ok_features=features_test[res==classes_test,:][:2]
#Bons Resultados
print("Resultados bem classificados:")
print("actual: ",classes_test[res!=classes_test])
print("predict:",res[res!=classes_test])
plt.figure()
for i,feat in enumerate(ok_features):
plt.subplot(1, 2, i+1)    
plt.imshow(feat.reshape(8,8), cmap='binary')

----

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets


# Dataset Digitos
digits = datasets.load_digits()

[features_train, features_test, classes_train, classes_test] = model_selection.train_test_split(digits.data, digits.target, test_size=0.30)
model = RandomForestClassifier(n_estimators=1000)

clf = model.fit(features_train, classes_train)

score_train = model.score(features_train, classes_train)
score_test = model.score(features_test, classes_test)

print("score_train:", score_train)
print("score_test:", score_test)