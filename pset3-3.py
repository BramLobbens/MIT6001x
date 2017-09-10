# MIT 6.00.1x Pset3-3

import string

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

#
# Version 1
#
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    checkList = []
    ans = ''
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            checkList.append(letter)

    return ans.join(checkList)

print(getAvailableLetters(lettersGuessed))

#
# Version 2
#
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    ans = ''
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            ans += letter

    return ans

print(getAvailableLetters(lettersGuessed))

#
# Version 3
#
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    ans = ''
    checkList = list(string.ascii_lowercase)
    for letter in checkList:
        if letter in lettersGuessed:
            checkList.remove(letter)

    return ans.join(checkList)

print(getAvailableLetters(lettersGuessed))