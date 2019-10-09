# -*- coding: utf-8 -*-
from optparse import OptionParser


def getArgs():
    parser = OptionParser()
    parser.add_option("-f", "--file", dest = "file")
    parser.add_option("-l", "--list_of_stopWords", dest = "listStop")
    parser.add_option("-n", "--topNwords", dest = "topN")
    return parser.parse_args()[0]

def makeStopSet(listStop):
    stopSet = set([])
    with open(listStop) as stops:
        for line in stops:
            line = line.strip()
            stopSet.add(line)
    return stopSet

def insertWord(word, count):
    print("inserting {0} {1}".format(word, count))
    global topWords
    global topCounts
    for i in range(0, len(topCounts)-1):
        print("i = {0}".format(i))
        if count > topCounts[i]:
            for j in range(len(topCounts)-1, i, -1):
                topCounts[j] = topCounts[j-1]
                topWords[j] = topWords[j-1]
            topCounts[i] = count
            topWords[i] = word
            print("===Current Result===")
            for word, count in zip(topWords, topCounts):
                print("{0}: {1}".format(word, count))
            return
  
        
def main():
    # get options
    myFile = getArgs().file
    myTopN = int(getArgs().topN)
    myList = getArgs().listStop
    if not myList == "None":
        myStopSet = makeStopSet(myList)
#    print(myStopSet)
#        
    # to strip list    
    punctuations = ''.join([chr(i) for i in range(33,65)])
    punctuations = punctuations + '“'
    # countWords
    wordCount = {}
    
    with open(myFile, encoding="utf-8") as file:
        for line in file:
            words = line.split()
     
            for word in words:
                word = word.lower()
                wordlower = word
                word = word.strip(punctuations)      
    #            print("====\n1. word = {0}".format(word))
                if not myList == 'None' and (word in myStopSet or wordlower in myStopSet):
    #                print("2. skipping word {0}".format(word) )
                    next
                else:
                    if word in wordCount:
                        wordCount[word] += 1
                        print("3. adding word {0} to wordcount, and count is {1}".format(word, wordCount[word]))
                    else:
                        wordCount[word] = 1
                        print("4. registering word {0} to wordcount and count is 1".format(word))
 
                    
    # populate topWords with dummy 10 words  
    global topWords
    topWords = []
    global topCounts
    topCounts = []
    for i in range(0, myTopN):
        dummy = 'dummy' + str(i)
        print(dummy)
        topWords.append(dummy)
        topCounts.append(0)
    
    # maintain the topWords by iterating through the remaining wordCount
    for word, count in wordCount.items():
        if count > topCounts[9]:
            insertWord(word, count)
        
    # print the results
    print("==============Final Result============")
    for word, count in zip(topWords, topCounts):
        print("{0}: {1}".format(word, count))
        
if __name__ == '__main__':
    main()
        

