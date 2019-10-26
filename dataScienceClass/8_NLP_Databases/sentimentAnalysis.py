# -*- coding: utf-8 -*-

import nltk
import string
from nltk.classify import NaiveBayesClassifier


def build_bag_of_words_features_filtered(words):
    return {word: 1 for word in words \
            if word not in words_to_filter}
    
punctuation = string.punctuation
stopWords = nltk.corpus.stopwords.words('English')
words_to_filter = stopWords + list(punctuation)

negative_features = [(build_bag_of_words_features_filtered(nltk.corpus.movie_reviews.words(f)), 'neg') \
                     for f in nltk.corpus.movie_reviews.fileids('neg')]
positive_features = [(build_bag_of_words_features_filtered(nltk.corpus.movie_reviews.words(f)), 'pos') \
                     for f in nltk.corpus.movie_reviews.fileids('pos')]
split = 800
sentiment_classifier = NaiveBayesClassifier.train(negative_features[:split] + positive_features[:split])
trainingAccuracy = nltk.classify.util.accuracy(sentiment_classifier, \
                                               negative_features[:split] + positive_features[:split]) * 100
print('Naive Bayes Classifier accuracy for training set is %.2f percent' % trainingAccuracy)
testAccuracy = nltk.classify.util.accuracy(sentiment_classifier, \
                                           negative_features[split:] + positive_features[split:]) * 100
print('Naive Bayes Classifier accuracy for testing set is %.2f percent' % testAccuracy)
sentiment_classifier.show_most_informative_features()


