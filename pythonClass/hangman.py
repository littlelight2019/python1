# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for l in secretWord:
        if not l in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessed = ''
    for l in secretWord:
        if not l in lettersGuessed:
            guessed += '_ '
        else:
            guessed += l
    return guessed



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    available = ''
    for l in string.ascii_lowercase:
        if not l in lettersGuessed:
            available += l
    return available	

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    length = len(secretWord)
    guessLeft = 8
    guessedLetters = {}
    guessedWord = '_ ' * length
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is %d letters long.' % length)
    while True:
        print('---------------')
        print('You have %d guesses left.' % guessLeft)
        available = getAvailableLetters(guessedLetters.keys())
        print('Available letters: %s' % available)
        letter = input('Please guess a letter: ')
        if letter in guessedLetters:
            print("Oops! You've already gussed that letter: %s" % guessedWord)
        else:
            guessedLetters[letter] = 1
            guessedWord = getGuessedWord(secretWord, guessedLetters.keys())
            if letter in secretWord:
                print('Good guess: %s' % guessedWord)
                if isWordGuessed(secretWord, guessedLetters.keys()):
                    print('---------------')
                    print('Congratulations, you won!')
                    break
            else:
                print('Oops! That letter is not in my word: %s' % guessedWord)
                guessLeft -= 1
                if guessLeft == 0:
                    print('Sorry, you ran out of guesses. The word was %s' % secretWord)
                    break
                
wordList = loadWords()
secretWord = chooseWord(wordList)
hangman(secretWord)