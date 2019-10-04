# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# read csv files into DataFrames
def readFiles():
    global movies
    global ratings
    movies = pd.read_csv('../4_pandas/movielens/movies.csv')
    ## clean up movie titles
    movies['title'] = movies['title'].str.strip()
    # extract year from title
    movies['year'] = movies['title'].str.extract('\((\d\d\d\d)\)$')

    ratings = pd.read_csv('../4_pandas/movielens/ratings.csv')
    #tags = pd.read_csv('../4_pandas/movielens/tags.csv')

# 1. get Genres list
def getGenresList():
    global genreslist
    global movies    
    GenresDic = {}
    GenresList = movies['genres'].unique().tolist()
    for words in GenresList:
        for genres in words.split('|'):
            if not genres in GenresDic:
                GenresDic[genres] = 1
    genreslist = sorted(GenresDic.keys())
    
# 2. get movieCount, ratingCount, avgRating by genres
def getRatingAndCountsByGenres():
    global ratings
    global movies
    global genreslist
    
    movieCount = []
    ratingCountByThousand = []
    avgRating = []
    for genres in genreslist:
        movieInGenres = movies[ movies['genres'].str.contains(genres) ]['movieId']
        print(type(movieInGenres))
        movieCount.append(movieInGenres.count())
        ratingInGenres = ratings.merge(movieInGenres, on = 'movieId', how = 'inner')['rating']
        ratingCountByThousand.append(ratingInGenres.count() / 1000)
        avgRating.append(ratingInGenres.mean())
# 3. put movieCount, ratingCount, avgRating into DataFrame with genreslist as index
#   and sort by avgRating    
    df = pd.DataFrame({'Movie Count': movieCount,
                       'Rating Count (thousands)': ratingCountByThousand,
                       'Avg Rating': avgRating}, index=genreslist)
    df = df.sort_values('Avg Rating')  
# 4.1  figure1: Avg Rating vs Genres (bar graph)
    plt.figure()
    df['Avg Rating'].plot.bar(figsize=(15,6), 
      title='Average Movie Rating By Genres', 
      fontsize=18)
# 4.2 figure2: Movie Count and rating count vs Genres (bar graph)
    plt.figure()
    df[['Movie Count', 'Rating Count (thousands)']].plot.bar(figsize = (15, 6),
      title = 'Movie Count and Rating Count By Genres', fontsize=18)
# 4.3 Rating Count vs Movie Count (scatter graph with annotation)
    plt.figure()
    fig, ax = plt.subplots()
    df.plot(x='Movie Count', y='Rating Count (thousands)', kind='scatter',
            title = 'Rating Count (thousands) vs Movie Count', figsize = (15,6), ax=ax)
    mydf = df.loc[['Sci-Fi','Action','Adventure','Documentary','Drama','Horror'], 
                  ['Movie Count','Rating Count (thousands)']]
    for k, v in mydf.iterrows():
        ax.annotate(k,v)
    rAll = df['Rating Count (thousands)'].corr(df['Movie Count'])
    mydfRest = df.drop(['Sci-Fi','Action','Adventure','Documentary','Drama','Horror'])
    rRest = mydfRest['Rating Count (thousands)'].corr(mydfRest['Movie Count'])   
    rMySet = mydf['Rating Count (thousands)'].corr(mydf['Movie Count'])   
    print('Correlation Coefficient for Rating Count (thousands) vs Movie Count:')
    print('For All Genres: %f' % rAll)
    print('For Sci-Fi,Action,Adventure,Documentary,Drama,Horror: %f' % rMySet)
    print('For Rest of Genres: %f' % rRest)
#
##### part II. By Year
#
def getYearlyRatingStat():
# 1. line plot for average ratings over the years
    global ratings
    global movies
    ratings = ratings.merge(movies[['movieId', 'year']],
           on = 'movieId', how = 'inner')
    yearly_rating_stat = ratings[['year','rating']].groupby('year')['rating'].describe()
    print(yearly_rating_stat.columns)
    plt.figure()
    yearly_rating_stat['mean'].plot.line(figsize=(15,6), 
                      title='Yearly Average Rating')
    yearly_rating_stat.index = pd.to_numeric(yearly_rating_stat.index).astype(np.int)
    df = pd.DataFrame({'year': range(1995,2016),
                       'rating': yearly_rating_stat.loc[range(1995,2016)]['mean']},
                        index = range(1995,2016))
    print(df.index.dtype)
    plt.figure()
    fig, ax1 = plt.subplots()
    ax1.locator_params(integer=True)
    df['rating'].plot.line(ax = ax1)
    for k, v in df.loc[[2012, 2014, 2015]].iterrows():
        ax1.annotate(k, v)

# 2: support yearly mean rating line plot conclusions by boxplot of 10-year-bin rating
def makeMovieIdYearBin():    
# 2.1. create new df movieIdYearBin
    global movieIdYearBin
    movieIdYearBin = movies[['movieId','year']]
    movieIdYearBin = movieIdYearBin.dropna()
    movieIdYearBin['year'] = pd.to_numeric( movieIdYearBin['year'])
    movieIdYearBin['bin'] = ((movieIdYearBin['year'] - 1891)/10).astype(np.int)

def makeBoxplotYearBinRating():
# 2.2 boxplots of ratings by 10-year-bin
# 2.2.1. labels
    yearStarts = [1891 + i*10 for i in range(0, 13)]
    yearEnds = [1900 + i * 10 for i in range(0, 13)]
    yearEnds[12] = 2015
    labels = [ (str(a) + '-' + str(b)) for a, b in zip(yearStarts, yearEnds)] 
# 2.2.2. np.ndarray
    data = []
    for bin in range(0, 13):
        data.append( movieIdYearBin[ movieIdYearBin['bin'] == bin].merge(ratings,
                    on = 'movieId', how = 'inner')['rating'])
# 2.2.3. boxplot figure
    plt.figure(figsize=(15,6))    
    plt.boxplot(data)
    plt.title('Movie Rating Over the Years')
    plt.xlabel('Years', labelpad=10)
    plt.xticks(np.arange(1, 14), labels, rotation=45)
    plt.ylabel('Rating')

#3. Movie Count and Rating Count over the years
def getCountsAndRatingOverYears():  
    global movieIdYearBin
    global ratings
    movieIdCount = movieIdYearBin.groupby('year')['movieId'].count()
    ratingByYear = movieIdYearBin.merge(ratings[['movieId','rating']], 
                                        on = 'movieId', how = 'inner')
    ratingCount = ratingByYear.groupby('year')['rating'].count()
    df = pd.DataFrame({'Movie Count': movieIdCount,
                       'Rating Count (thousands)': ratingCount / 1000})
    # global line plot
    plt.figure()
    df.plot.line(figsize=(15,6), 
                 title='Movie Count and Rating Count over the Years')
    # insert zoom in to peak years
    plt.figure()
    fig, ax1 = plt.subplots()
    df.loc[range(1990,2016)].plot.line(ax = ax1)
    # annotate the peaks
    mydf = pd.DataFrame({'year': [1995, 1999],
                         'rating': df.loc[[1995,1999]]['Rating Count (thousands)']},
                        index = [1995, 1999])
    for k, v in mydf.iterrows():
        ax1.annotate(k, v)
    mydf = pd.DataFrame({'year': [2009,2013],
                         'count': df.loc[[2009,2013]]['Movie Count']},
                        index = [2009, 2013])
    for k, v in mydf.iterrows():
        ax1.annotate(k, v)
    

          


