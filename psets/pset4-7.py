# MIT 6.00.1x Pset4-7

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    current_hand = None

    while True:
        game_choice = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        
        if game_choice == 'n':
            current_hand = dealHand(HAND_SIZE)
            while True:
                player_choice = input('Enter u to have yourself play, c to have the computer play: ')

                if player_choice == 'u':
                    playHand(current_hand, wordList, HAND_SIZE)
                    break
                elif player_choice == 'c':
                    compPlayHand(current_hand, wordList, HAND_SIZE)
                    break
                else:
                    print('Invalid command.')

        elif game_choice == 'r':
            if current_hand == None:
                print('You have not played a hand yet. Please play a new hand first!')
            else:
                while True:
                    player_choice = input('Enter u to have yourself play, c to have the computer play: ')
                    if player_choice == 'u':
                        playHand(current_hand, wordList, HAND_SIZE)
                        break
                    elif player_choice == 'c':
                        compPlayHand(current_hand, wordList, HAND_SIZE)
                        break
                    else:
                        print('Invalid command.')

        elif game_choice == 'e':
            break
        else:
            print('Invalid command.')

    return None
