# MIT 6.00.1x Pset4-3

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    check_hand = hand.copy()
    for letter in word:
    
        if letter not in check_hand.keys() or check_hand[letter] <= 0:
            return False
        check_hand[letter] -= 1
    
    return word in wordList