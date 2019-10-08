# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import sqlite3
from math import sqrt

def dataIngestion():
    cnx = sqlite3.connect('C:/Users/qjane/dev/sqlite/soccer.sqlite')
    df = pd.read_sql_query('select * from Player_Attributes', cnx)
    df = df.dropna()
    features = ['potential']
    features.extend(df.columns.tolist()[9:])
    X = df[features]
    y = df[['overall_rating']]
    return X, y

def splitTrainTestSets(X, y, testSize, randomState):
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size = testSize,
                                                        random_state = randomState)
    return X_train, X_test, y_train, y_test

def trainLinerModel(X, y):
    regressor = LinearRegression()
    regressor.fit(X, y)
    return regressor

def trainDecisionTreeModel(X, y):
    regressor = DecisionTreeRegressor(max_depth=20)
    regressor.fit(X, y)
    return regressor

def evalModel(model, X, yTrue):
    prediction = model.predict(X)
    mse = mean_squared_error(y_true = yTrue, y_pred = prediction)
    return sqrt(mse)

def main():
    X, y = dataIngestion()
    X_train, X_test, y_train, y_test = splitTrainTestSets(X, y, 0.33, 324)
    linearRegressor = trainLinerModel(X_train, y_train)
    print('Linear Regression Model RMSE for testSet: %f' % 
          evalModel(linearRegressor, X_test, y_test))
    print('Linear Regression Model RMSE for trainingSet: %f' %
          evalModel(linearRegressor, X_train, y_train))
    decisionTreeRegressor = trainDecisionTreeModel(X_train, y_train)
    print('Decision Tree Regression Model RMSE for testSet: %f' % 
          evalModel(decisionTreeRegressor, X_test, y_test))
    print('Decision Tree Regression Model RMSE for trainingSet: %f' %
          evalModel(decisionTreeRegressor, X_train, y_train))
    
if __name__ == '__main__':
    main()    