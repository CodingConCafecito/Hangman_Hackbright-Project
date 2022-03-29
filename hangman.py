import random
# import random library to be able to assign a random mystery word to the player

from words import word_list

def picking_mystery_word():
    #returns  random mystery word that player has to guess 
    word = random.choice(word_list).upper()
    return word
    
def introducing_game():
    # welcomes the player and explains the game
    print()
    print("Welcome! \n\nSave PEPINO the 🐍 from BENITO the 🦅 by figuring out what the 5 letter mystery word is. \n\nYou only have 9 chances to help PEPINO 🐍 escape! \n\nGood luck!")

def print_emoji_status(attempts_available):
    # prints how far 🐍 and 🦅 are from eachother    
    if attempts_available == 9:
        print ("""
         ....... 🦅💨
    .......
         .......
    .......
         .......
    .......
         .......
    .......
         .......
    🐍 😎""")
    elif attempts_available == 8:
        print ("""
    ....... 🦅💨
         .......
    .......
         .......
    .......
         .......
    .......
         .......
    🐍 😌""")
    elif attempts_available == 7:
        print ("""
         ....... 🦅💨
    .......
         .......
    .......
         .......
    .......
         .......
    🐍 😗""")
    elif attempts_available == 6:
        print("""
    ....... 🦅💨
         .......
    .......
         .......
    .......
         .......
    🐍 🙄""")
    elif attempts_available == 5:
        print("""
         ....... 🦅💨
    .......
         .......
    .......
         .......
    🐍 🤔""")
    elif attempts_available == 4:
        print("""
    ....... 🦅💨
         .......
    .......
         .......
    🐍 🤨""")
    elif attempts_available == 3:
        print("""
         ....... 🦅💨
    .......
         .......
    🐍 😮""")
    elif attempts_available == 2:
        print("""
    ....... 🦅💨
         .......
    🐍 😨""")
    elif attempts_available == 1:
        print("""
         ....... 🦅💨
    🐍 🆘""")
    else:
        print("""
         💥🦅
    🐍 😱""")


def play_game(mystery_word):
    #updates variables, validates guesses, checks if player wins/loses
    mystery_word_display = "_" * len(mystery_word)
    game_over = False
    letters_guessed = []
    attempts_available = 9
    print_emoji_status(attempts_available)
    print()
    print("Mystery Word:", mystery_word_display, "🔍")
    
    while not game_over and attempts_available > 0:
        print()
        print ("Please guess a letter.\n")
        guess = input("> ").upper()
        print()
        if len(guess) == 1 and guess.isalpha(): # has to be one letter long and an alphabetical letter
            if guess in letters_guessed:
                print("You've already guessed ", guess, ". Try again!")
            elif guess in mystery_word:
                letters_guessed.append(guess)
                attempts_available = attempts_available - 1 # move to a function with above line?
                print("Yippie! 🐍\n")
                print("🌟 Correct guess!", guess,"is in the mystery word.")

                mystery_word_list = list(mystery_word_display) # makes mystery_word_status_display a list
                
                for i, letter in enumerate(mystery_word):
                    if letter == guess:
                        mystery_word_list[i] = guess # if letter == guess, then at that index of this  list, the "_" is replaced with the letter guessed
                        mystery_word_display = "".join(mystery_word_list) # joins all the elements in the list

                if "_" not in mystery_word_display:
                    game_over = True

            else: #if guess not in mystery_word
                letters_guessed.append(guess)
                attempts_available = attempts_available - 1
                print("Muhaha! 🦅\n")
                print("🚨 Incorrect guess!", guess,"is not in the word.")

        else: #if they don't input a single letter or an alphabetical letter
            print("Invalid entry. Please try again!")
        
        print_emoji_status(attempts_available)
        print()
        print("Chances Left:", attempts_available)
        print()
        print("Mystery Word:", mystery_word_display, "🔍")
        
    if game_over: #once game_over = True 
        print("\nCongrats, you found the mystery word! 🎉 \nPEPINO IS SAFE! 💕 🐍")
    else:
        print("\nOh no! 😭 BENITO flew away with PEPINO. 🦅 \n\nThe mystery word was:", mystery_word, "👀")
    print()
    
def replay_game():
    # asks player if they want to play again
    while True:
        choice = input("Want to play again? Enter Y for yes or N for No. \n> ").upper() # \n prints what follows on another line
        if choice == "Y" or choice == "N":
            return choice
        else:
            print("Please enter Y or N.")

def start_hangman():
    # houses the functions that run the game
    while True:
        mystery_word = picking_mystery_word()
        introducing_game()
        play_game(mystery_word)
        choice = replay_game()
        if choice == "N":
            print("Goodbye!")
            break
        else:
            print("Awesome! Good luck. 🤗")

start_hangman()

#NICE TO HAVES:
""" > Use colorama library to customize the color of the text
    > Use time library to edit how fast/slow specific code is executed
    > Personalize the game more by asking for their name"""

# FUTURE UPDATES:
""" 
> Player can guess the entire word 
> Player can choose level of difficulty which changes how many attempts they have available to them
> Player can choose a theme for the mystery words they are guessing. Each theme pulls up a different list of mystery words.
> Make a version en Espanol :)
> If sounds can be played from terminal, add sounds """
