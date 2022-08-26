# -*- coding: utf-8 -*-
"""Bank_note_authentiaction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fWJNqdutIQb-cCQUrg6dALaUxHEseBEk
"""

import pandas as pd

import numpy as np

import matplotlib.pyplot as ply

import seaborn as sns

df= pd.read_csv('https://www.dropbox.com/s/5sirw6tdflbo31b/BankNoteAuthentication.csv?dl=1')

df.head()

df.info()

df.describe(include='all')

df.describe(include='all')

df.corr()

df['entropy'].value_counts()

sns.pairplot(df, x_vars= ['variance','skewness','curtosis','entropy','class'], y_vars=['variance'])

sns.pairplot(df, x_vars= ['variance','skewness','curtosis','entropy','class'], y_vars=['skewness'])

sns.pairplot(df, x_vars= ['variance','skewness','curtosis','entropy','class'], y_vars=['curtosis'])

sns.pairplot(df, x_vars= ['variance','skewness','curtosis','entropy','class'], y_vars=['entropy'])

sns.pairplot(df, x_vars= ['variance','skewness','curtosis','entropy','class'], y_vars=['class'])

df.columns

x = df.iloc[:,:-1]

y = df.iloc[:,-1]

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test= train_test_split(x,y,train_size=0.7, random_state=192529)

x_train.shape,x_test.shape,y_train.shape,y_test.shape

from sklearn.ensemble import RandomForestClassifier

rfc=RandomForestClassifier
rfc_object = rfc(n_estimators=2000, random_state=0)

rfc_object.fit(x_train,y_train)

predicted_labels = rfc_object.predict(x_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(classification_report(y_test, predicted_labels)) 

print(confusion_matrix(y_test, predicted_labels)) 

print(accuracy_score(y_test, predicted_labels))

