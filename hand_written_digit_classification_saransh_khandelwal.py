# -*- coding: utf-8 -*-
"""Hand Written digit classification_Saransh_Khandelwal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K_goBvQgz0hg93cFDRjwTwNUjAJht8_V

##**Hand Written digit classification**

##**Import necessary libraries**
"""

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

"""##**Import data**"""

from sklearn.datasets import load_digits

df=load_digits()

_, axes = plt.subplots(nrows=1, ncols=5, figsize= (10,3))
for ax, image, label in zip(axes, df.images, df.target): 
  ax.set_axis_off()
  ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
  ax.set_title("Training: %i" % label)

df.images.shape

df.images[0]

df.images[0].shape

n_samples= len(df.images)
data=df.images.reshape((n_samples, -1))

df.images[0]

df.images[0].shape

n_samples= len(df.images)
data=df.images.reshape((n_samples, -1))

data[0]

data[0].shape

data.shape

"""##**Scaling data**"""

data.min()

data.max()

data=data/16

data.min()

data.max()

"""##**Train test split**"""

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test= train_test_split(data, df.target,train_size=0.7, random_state=2529)

X_train.shape,X_test.shape,y_train.shape,y_test.shape

"""##**Random forest model**"""

from sklearn.ensemble import RandomForestClassifier

rf=RandomForestClassifier()

rf.fit(X_train,y_train)

"""##**Predict test data**"""

y_pred =rf.predict(X_test)

y_pred

"""##**Model Accuracy**"""

from sklearn.metrics import confusion_matrix, classification_report

confusion_matrix (y_test, y_pred)

print(classification_report(y_test, y_pred))

