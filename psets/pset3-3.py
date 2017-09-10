# MIT 6.00.1x Pset3-3

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    ans = ''
    checkList = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        if letter in checkList:
            checkList.remove(letter)
    return ans.join(checkList)