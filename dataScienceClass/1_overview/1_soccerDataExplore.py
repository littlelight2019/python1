# -*- coding: utf-8 -*-
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale

# connect to DB and read table into dataframe
cnx = sqlite3.connect('C:/Users/qjane/dev/sqlite/soccer.sqlite')
df = pd.read_sql_query('select * from Player_Attributes', cnx)

# clean up: delete rows with na
df.isnull().any().any()
rows_total = df.shape[0]
df = df.dropna()
print("deleted rows with NA: %d" % (df.shape[0] - rows_total))

# shuffle the rows
df = df.reindex(np.random.permutation(df.index))

# define columns to run correlation with overall_rating
cols = ['potential',  'crossing', 'finishing', 'heading_accuracy',
       'short_passing', 'volleys', 'dribbling', 'curve', 'free_kick_accuracy',
       'long_passing', 'ball_control', 'acceleration', 'sprint_speed',
       'agility', 'reactions', 'balance', 'shot_power', 'jumping', 'stamina',
       'strength', 'long_shots', 'aggression', 'interceptions', 'positioning',
       'vision', 'penalties', 'marking', 'standing_tackle', 'sliding_tackle',
       'gk_diving', 'gk_handling', 'gk_kicking', 'gk_positioning',
       'gk_reflexes']

correlations = [ df['overall_rating'].corr(df[f]) for f in cols ]


# plot overall_rating against correlations
def plot_dataframe(df, y_label):
    color = 'coral'
    fig = plt.gcf()
    fig.set_size_inches(10, 6)
    plt.ylabel(y_label)
    
    ax = df.correlation.plot(linewidth=3.3, color=color)
    ax.set_xticks(df.index)
    ax.set_xticklabels(df.attributes, rotation=75)
    plt.show()
    
df2 = pd.DataFrame({'attributes': cols, 'correlation': correlations})    
plot_dataframe(df2, 'Player\'s Overall Rating')

# select 5 features to run k-means clustering
select5features = ['gk_kicking', 'potential', 'marking', 'interceptions', 'standing_tackle']
#selectedCorrelations = [df['overall_rating'].corr(df[f]) for f in select5features]
#for f, c in zip(select5features, selectedCorrelations):
#    print("%s: %f" % (f,c))
df_select = df[select5features].copy(deep=True)
data = scale(df_select)
model = KMeans(init='k-means++', n_clusters=4, n_init=20).fit(data)
print("==Counts for each cluster:==")
print(pd.value_counts(model.labels_, sort=False))

p = pd.DataFrame(model.cluster_centers_, columns=select5features)
p = p.join(pd.DataFrame({'prediction': [label for label in range(0,4)]}))
print(p)

#matplotlib.pyplot example
np.random.seed(19680801)
data = np.random.randn(2, 100)

fig, axs = plt.subplots(2, 2, figsize=(5, 5))
axs[0, 0].hist(data[0])
axs[1, 0].scatter(data[0], data[1])
axs[0, 1].plot(data[0], data[1])
axs[1, 1].hist2d(data[0], data[1])

plt.show()



