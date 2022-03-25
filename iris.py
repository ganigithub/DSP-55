import pandas as pd
import numpy as np
import pickle    #storing model model in a specific format
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

print("All libraries loaded")

#read in the iris data
iris = load_iris()

#create x and y
x = iris.data
y = iris.target

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

knn = KNeighborsClassifier(n_neighbors = 4)
knn.fit(x_train, y_train)

print("Model Building Finished")

#saving the model in .pkl forma
pickle.dump(knn, open('iris_knn.pkl', 'wb'))  #wb is for writing book

print("Pickle file dumped")
