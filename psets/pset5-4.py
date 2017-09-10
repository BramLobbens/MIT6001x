# MIT 6.00.1x Pset5-4

def decrypt_story():
    encoded_story = get_story_string()

    ciphertext = CiphertextMessage(encoded_story)
    
    return ciphertext.decrypt_message()