# MIT 6.00.1x Pset4-1

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # Validate word is a string
    assert isinstance(word, str)
    
    letters = []
    for letter in word:
        letters.append(letter)
    
    # Sum of points from SCRABBLE_LETTER_VALUES of letters that are in letters[]
    score = 0
    for letter in letters:
        if letter in SCRABBLE_LETTER_VALUES:
            score += SCRABBLE_LETTER_VALUES[letter]
    # Multiply score by length of word
    score *= len(word)
    # Additional 50 points if all letters in hand are used
    if len(word) == n:
        score += 50

    return score