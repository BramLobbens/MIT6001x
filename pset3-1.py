# MIT 6.00.1x Pset3-1

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

#
# Version 1
#
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    checkList = []
    
    for letter in secretWord:
        if letter in lettersGuessed:
            checkList.append(letter)
            
    print('lettersguessed:\t{0}\ncheckList:\t{1}'.format (lettersGuessed, checkList))
    
    if checkList == list(secretWord):
        return True
    else:
        return False
    
print(isWordGuessed(secretWord, lettersGuessed))

#
# Version 2
#
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
    
print(isWordGuessed(secretWord, lettersGuessed))


#
# Version 3
#
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

print(isWordGuessed(secretWord, lettersGuessed))