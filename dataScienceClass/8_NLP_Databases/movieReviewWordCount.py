# -*- coding: utf-8 -*-

import nltk
import matplotlib.pyplot as plt
import string
from collections import Counter

# Get a list of filtered words
punctuations = string.punctuation
stopwords = nltk.corpus.stopwords.words('english')
words_to_filter = stopwords + list(punctuations)
all_words = nltk.corpus.movie_reviews.words()
filtered_words = [word for word in all_words \
                  if word not in words_to_filter]
# Count the frequency of each word
wordCounter = Counter(filtered_words)
print(wordCounter.most_common()[:10])
# Distribution of word count in descending order
sortedWordCount = sorted(wordCounter.values(), reverse = True)
plt.figure(figsize = (10, 6))
plt.loglog(sortedWordCount)
plt.title('Distribution of Word Count in Movie Reviews')
plt.xlabel('Word Rank')
plt.ylabel('Frequency')
plt.show()
# Histogram of word counts
plt.figure(figsize = (10, 6))
plt.hist(sortedWordCount, bins = 80, log=True)
plt.title('Histogram of Word Count in Movie Reviews')
plt.xlabel('Frequency of the Word')
plt.ylabel('Count of Different Words')
plt.show()
