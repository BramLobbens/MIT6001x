# MIT 6.00.1x Pset3-1

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    checkList = [] # checklist to store guessed letters in secret word
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
        else:
            checkList.append(letter)
            
    return checkList == list(secretWord)