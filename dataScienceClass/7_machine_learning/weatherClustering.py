# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from pandas.plotting import parallel_coordinates
import matplotlib.pyplot as plt
from itertools import islice, cycle

def dataIngestion():
    data = pd.read_csv('weather/minute_weather.csv')
    sample_df = data[data.iloc[:, 0] % 10 == 0]
    sample_df = sample_df.dropna()
    columnIndex = [x for x in range(2,8)]
    columnIndex.append(12)
    select_df = sample_df.iloc[:,columnIndex]
    return select_df

def KmeansClustering(df):
    normalized_data = StandardScaler().fit_transform(df)
    cluster = KMeans(n_clusters=12)
    model = cluster.fit(normalized_data)
    return model
    
def pd_centers(features, centers):
    features.append('prediction')
    data = [np.append(mycenters, myindex) for myindex, mycenters in enumerate(centers)]
    P = pd.DataFrame(data, columns = features)
    P['prediction'] = P['prediction'].astype(np.int)
    return P

def parallel_plotbk(data, title):
    plt.figure()
    fig, ax = plt.subplots(figsize=(10,6))
    ax.set_ylim([-3, 3])
    ax.set_title(title)
    ax.set_xlabel('Weather Features')
    ax.set_ylabel('Standard Deviation')
    ax.tick_params(labelrotation = 20)
    my_colors = list(islice(cycle(['r','g','b','y','k']), None, len(data)))
    parallel_coordinates(data, 'prediction', color = my_colors, marker = 'o')

def parallel_plot(data, title):
    plt.figure(figsize = (10,6))
    plt.ylim([-3, 3])
    plt.title(title)
    plt.xlabel('Weather Features')
    plt.ylabel('Standard Deviation')
    plt.tick_params(labelrotation = 20)
    my_colors = list(islice(cycle(['r','g','b','y','k']), None, len(data)))
    parallel_coordinates(data, 'prediction', color = my_colors, marker = 'o')
    
def main():
    df = dataIngestion()
    KmeansModel = KmeansClustering(df)
    centers = KmeansModel.cluster_centers_
    centersDF = pd_centers(df.columns.tolist(), centers)
    
    low_humidity_centers = centersDF[centersDF['relative_humidity'] < -0.5]
    parallel_plot(low_humidity_centers, 'Low Humidity Centers')
    
    warm_centers = centersDF[centersDF['air_temp'] > 0.5]
    parallel_plot(warm_centers, 'Warm Centers')
    
    cool_centers = centersDF[(centersDF['relative_humidity'] > 0.5) &
                             (centersDF['air_temp'] < 0.5)]
    parallel_plot(cool_centers, 'Cool Centers')
    
    
 
    


if __name__ == '__main__':
    main()
