# MIT 6.00.1x Pset3-4

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
    guesses = []    # Store guesses made
    mistakes = 8    # Number of mistakes allowed
    
    print('Welcome to the game, Hangman!\n' +
            'I am thinking of a word that is ' +
            '{0} letters long'.format(len(secretWord)))
            
    print('-'*11) # -----------
    
    while not isWordGuessed(secretWord, guesses):
        
        print('You have {0} guesses left'.format(mistakes))
        #print('Your guesses:',guesses)
        availableLetters = getAvailableLetters(guesses)
        print('Available letters:', availableLetters)
        answer = getGuessedWord(secretWord, guesses)
        
        while True:
            
            guess = input('Please guess a letter: ').lower()
            guesses.append(guess)
            answer = getGuessedWord(secretWord, guesses)
            if guess in availableLetters:
                break
            else:
                print('Oops! You\'ve already guessed that letter:',answer)
                print('-'*11) # -----------
                print('You have {0} guesses left'.format(mistakes))
        
        if guess in secretWord:
            print('Good guess:', answer)
        
        elif guess not in secretWord:
            mistakes -= 1
            print('Oops! That letter is not in my word:',answer)
            
        if mistakes == 0:
            print('-'*11) # -----------
            print('Sorry, you ran out of guesses. The word was {0}.'.format(secretWord))
            return None
            break
        
        print('-'*11) # -----------
    
    if answer == secretWord:
        print('Congratulations, you won!')
    
    return None