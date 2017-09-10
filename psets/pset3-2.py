# MIT 6.00.1x Pset3-2

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    checkList = []
    ans = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            checkList.append(letter)
        else:
            checkList.append('_ ')
    return ans.join(checkList)