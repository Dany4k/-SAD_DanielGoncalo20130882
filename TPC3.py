#Importar os módulos para o funcionamento
from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

#Importar e ver a tabela
data = datasets.california_housing.fetch_california_housing()
data

dframe = pd.DataFrame(data.data, columns=data.feature_names)
dframe.head()

#1)Aggregation
stat = dframe.groupby("MedInc").agg(["mean","count", "std"])
stat

#2)Sampling
X = dframe.groupby("Population").agg("max")
X

#3)Dimensionality Reduction
dframe.dropna(axis=1)

#4)Feature Subset Selection
dframe[:3]

#5)Feature Creation 
def my_func(x):
    return [x[0],x.name**2,x.name*x[1]]
  
my_func

#6)Binarization
binarizer = preprocessing.Binarizer().fit(X)
print(binarizer)
binarizer.threshold=3.5
print(X[0:5,:])
binarizer.transform(X)[:5,:]