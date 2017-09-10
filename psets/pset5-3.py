# MIT 6.00.1x Pset5-3

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        previous_count = 0
        count = 0
        best_shift = {}
        best_decoded = ''

        for s in range(1, 26):
            shift = s
            decoded = self.apply_shift(shift)

            words = decoded.split(':')
            temp = ''

            for word in words:
                temp += ''.join(word.lower())

            words = temp.split(' ')
            
            count = 0
            
            for word in words:
                if word in self.valid_words:
                    count += 1

            best_shift.update({s: count})
            if count > previous_count:
                best_decoded = decoded
            previous_count = count
            

        best_value = max(best_shift.values())
        for key, value in best_shift.items():
            if value == best_value:
                return key, best_decoded