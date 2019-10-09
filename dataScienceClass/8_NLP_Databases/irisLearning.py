# -*- coding: utf-8 -*-

import sqlite3
import pandas as pd
from pandas.plotting import parallel_coordinates
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.model_selection import train_test_split
from math import sqrt

def dataIngestion():
    conn = sqlite3.connect('C:/Users/qjane/dev/sqlite/iris.sqlite')
    df = pd.read_sql_query('select * from Iris', conn)
    return df

def featureSelection(features, df):
    return df[features]

def defineTrainTestSets(X, y, testSize, randomState):
    return train_test_split(X, y, test_size = testSize, random_state = randomState)

def trainDecisionTreeClassifierModel(X, y):
    model = DecisionTreeClassifier(max_depth = 20)
    model.fit(X, y)
    return model

def trainDecisionTreeRegressorModel(X, y):
    model = DecisionTreeRegressor(max_depth = 20)
    model.fit(X, y)
    return model

def trainLinearRegressionModel(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model

def trainKmeansModel(X, numCluster):
    normalizedData = StandardScaler().fit_transform(X)
    model = KMeans(n_clusters = numCluster)
    model.fit(normalizedData)
    return model
    
def modelEvalAccuracy(model, X, y):
    prediction = model.predict(X)
    return accuracy_score(y_true = y, y_pred = prediction)

def modelEvalRMSE(model, X, y):
    prediction = model.predict(X)
    mse = mean_squared_error(y_true = y, y_pred = prediction)
    return sqrt(mse)

def parallel_plot(df, label):
    my_colors = ['r', 'g', 'b']
    plt.figure()
    fig, ax = plt.subplots(figsize = (10, 6))
    ax.set_title('Clusters of iris')
    ax.set_xlabel('Flower Features')
    ax.set_ylabel('Standard Deviations')
    ax.tick_params(labelrotation = 20)
    parallel_coordinates(df, label, color = my_colors, marker = 'o')
    
def main():
    df = dataIngestion()
    # Decision Tree Classifier
    treeClassifierFeatures = df.columns.tolist()[1:5]
    treeClassifierTarget = df.columns.tolist()[5]
    treeClassifierX = featureSelection(treeClassifierFeatures, df)
    treeClassifierY = featureSelection(treeClassifierTarget, df)
    X_train, X_test, y_train, y_test = defineTrainTestSets(treeClassifierX, treeClassifierY, 0.25, 324)
    treeClassifierModel = trainDecisionTreeClassifierModel(X_train, y_train)
    print('Decision Tree Classifier Model Accuracy for TestData is %f' %
          modelEvalAccuracy(treeClassifierModel, X_test, y_test))
    print('Decision Tree Classifier Model Accuracy for TrainData is %f' %
          modelEvalAccuracy(treeClassifierModel, X_train, y_train))
    # Decision Tree Regressor and Linear Regressor
    regressionFeatures = df.columns.tolist()[1:4]
    regressionTarget = df.columns.tolist()[4]
    regressionX = featureSelection(regressionFeatures, df)
    regressionY = featureSelection(regressionTarget, df)
    X_train, X_test, y_train, y_test = defineTrainTestSets(regressionX, regressionY, 0.25, 324)
    treeRegressorModel = trainDecisionTreeRegressorModel(X_train, y_train)
    print('Decision Tree Regressor Model RMSE for TestData is %f' %
          modelEvalRMSE(treeRegressorModel, X_test, y_test))
    print('Decision Tree Regressor Model RMSE for TrainData is %f' %
          modelEvalRMSE(treeRegressorModel, X_train, y_train))
    LinearRegressorModel = trainLinearRegressionModel(X_train, y_train)
    print('Linear Regressor Model RMSE for TestData is %f' %
          modelEvalRMSE(LinearRegressorModel, X_test, y_test))
    print('Linear Regressor Model RMSE for TrainData is %f' %
          modelEvalRMSE(LinearRegressorModel, X_train, y_train))
    # K-means clustering
    X = treeClassifierX
    kmeansModel = trainKmeansModel(X, 3)
    clusterCenters = kmeansModel.cluster_centers_ 
    columnNames = X.columns.tolist()
    kmeansDF = pd.DataFrame(data = clusterCenters, columns = columnNames)
    labelColumn = ['Cluster #' + str(i) for i in range(1,4)]
    labelDF = pd.DataFrame({'clusterLabel': labelColumn})            
    kmeansDF = kmeansDF.join(labelDF)
    kmeansDF = kmeansDF.sort_values('SepalLengthCm')
    print(kmeansDF)
    parallel_plot(kmeansDF, 'clusterLabel')
    ## compare with species data
    normalized = StandardScaler().fit_transform(df.iloc[:,1:5])
    myDF = pd.DataFrame(normalized, columns = df.columns.tolist()[1:5])
    myDF = myDF.join(df['Species'])
    myDF.sort_values('SepalLengthCm')
    parallel_plot(myDF,'Species')
    
    
if __name__ == '__main__':
    main()