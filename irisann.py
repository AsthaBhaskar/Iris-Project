# -*- coding: utf-8 -*-
"""IrisANN

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kbcGIyAP7Z0SBkkTCe1nK8XUJPoa7myY
"""

# Importing Packages
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn import datasets

"""The Iris dataset has 150 observations or Rows and 5 atttibutes or Columns of Iris Flowers.

First four columns are - **Sepal Length, Sepal Width , Petal Length, Petal Width**, all are in cm.


---


The Last column is containing the Classes - **['setosa' 'versicolor' 'virginica']**


---


As we are loading the dataset from sklearn, the dataset is already pre-processed.

**So, the Classes are - [ 0 , 1 , 2 ] instead of ['setosa' 'versicolor' 'virginica'].**
"""

# Loading Dataset
data = datasets.load_iris()
print(data)

x = data.data
y = data.target
z = data.target_names
print(data.feature_names)
print(x[0])

# Split Dataset
from sklearn.model_selection import train_test_split
x_train, x_test,  y_train, y_test = train_test_split(x, y, test_size=0.3)

# Data Shape
print(x_train.shape)
print(x_test.shape)

# Building the Model
model= Sequential()
model.add(Dense(100,input_shape=(4,), activation="relu"))
model.add(Dense(3, activation='softmax'))

# Compile the Model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Fit the Model
model.fit(x_train,y_train, epochs=20)

# Evaluate the Model
model.evaluate(x_test, y_test)

# Predict for the first 10 Observations
pred=model.predict(x_test[:10])
print(pred)

p=np.argmax(pred, axis=1)
print(p)
print(y_test[:10])

# Prediction Result
for i in p:
  print("Predicted-Class: {},   Name: {}".format(i,z[i]))