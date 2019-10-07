# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv('./weather/daily_weather.csv')
clean_data = data.copy()
clean_data = clean_data.dropna()
del clean_data['number']

morningFeatures = clean_data.columns[0:9].tolist()
x = clean_data[morningFeatures]
y = (clean_data['relative_humidity_3pm'] > 24.99) * 1
y.name = 'high_humidity_label'
print(y.name)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state = 324)
humidity_classifier = DecisionTreeClassifier(max_leaf_nodes=10, random_state = 0)
humidity_classifier.fit(x_train, y_train)

testAccuracy = accuracy_score(y_true = y_test, y_pred = humidity_classifier.predict(x_test))
trainAccuracy = accuracy_score(y_true = y_train, y_pred = humidity_classifier.predict(x_train))
print('Test accuracy is %f' % testAccuracy)
print('Train accuracy is %f' % trainAccuracy)