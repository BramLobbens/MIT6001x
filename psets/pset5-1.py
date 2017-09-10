# MIT 6.00.1x Pset5-1

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''

        assert shift >= 0 and shift < 26

        def shift_char(char):
            # lowercase letters
            if char.islower():
                return chr(((ord(char) - 97) + shift) % 26 + 97)
            # uppercase letters
            elif char.isupper():
                return chr(((ord(char) - 65) + shift) % 26 + 65)
            # Ignore non-alphabetical characters
            else:
                return char

        shift_dict = {char: shift_char(char) for char in string.ascii_letters}

        return shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        
        shift_dict = self.build_shift_dict(shift)
        encoded = ''

        for letter in self.message_text:
            try:  # alphabetical letter that can be converted
                encoded += ''.join(shift_dict.get(letter))
            except TypeError:  # non-alphabetical character
                encoded += ''.join(letter)

        return encoded