import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")

    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = str.split(line)
    print("  ", len(wordlist), "words loaded.")
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    secretLetters = []

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True


def getGuessedWord(secretWord, lettersGuessed):
    guessed = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '

    return guessed


def getAvailableLetters(lettersGuessed):
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase

    for letter in available:
        if letter in lettersGuessed:
            available = available.replace(letter, '')

    return available


def hangman(secretWord):

    guesses = 8
    lettersGuessed = []
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    print('-------------')

    while not isWordGuessed(secretWord, lettersGuessed) and guesses > 0:
        print('You have ', guesses, 'guesses left.')

        available = getAvailableLetters(lettersGuessed)
        print('Available letters', available)

        letter = input('Please, guess a letter: ')
        if letter in lettersGuessed:

            guessed = getGuessedWord(secretWord, lettersGuessed)

            print('Oops! You have already guessed that letter: ', guessed)
        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = getGuessedWord(secretWord, lettersGuessed)

            print('Good Guess: ', guessed)
        else:
            guesses -= 1
            lettersGuessed.append(letter)

            guessed = getGuessedWord(secretWord, lettersGuessed)
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print('Oops! That letter is not in my word: ',  guessed)
        print('------------')

    else:
        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
        else:
            print('Sorry, you ran out of guesses. \
            The word was ', secretWord, '.')

            count = input('Press y to play again or any key to go out\n\n\n')
            if count == 'y':
                print('\n\n Glad you are back! Keep Trying!!')
                hangman(secretWord)
            else:
                print('See you later alligator!')


secretWord = loadWords().lower()
hangman(secretWord)
