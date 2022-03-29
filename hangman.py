# This is a variation of the game hangman.
# Player needs to guess the 5 letter mystery word before the 🦅 (eagle) reaches the 🐍 (snake).

import random
# import random library to be able to assign a random mystery word to the player

""" from words import word_list """
#import list that is on a separate python file that contains the mystery words
word_list = ["hello", "blues", "berry", "house"] # test out with a few words first

def picking_mystery_word():
    #returns  random mystery word that player has to guess 
    word = random.choice(word_list).upper()
    return word
    
def introducing_game():
    # welcomes the player and explains the game
    print()
    print("Welcome!")
    print("Save PEPINO the 🐍 from BENITO the 🦅 by figuring out what the mystery word is. You have 6 chances to help PEPINO 🐍 escape! Good luck!")

def print_emoji_status(attempts_available):
    # prints how far 🐍 and 🦅 are from eachother    
    if attempts_available == 7:
        print ("""
        ...... 🦅💨
    ......
        ......
    ......
        ......
    ......
        ......
    🐍 😎""")
    elif attempts_available == 6:
        print("""
    ...... 🦅💨
        ......
    ......
        ......
    ......
        ......
    🐍❓""")
    elif attempts_available == 5:
        print("""
        ...... 🦅💨
    ......
        ......
    ......
        ......
    🐍🤔""")
    elif attempts_available == 4:
        print("""
    ...... 🦅💨
        ......
    ......
        ......
    🐍🤨""")
    elif attempts_available == 3:
        print("""
        ...... 🦅💨
    ......
        ......
    🐍🤨""")
    elif attempts_available == 2:
        print("""
    ...... 🦅💨
        ......
    🐍🤨""")
    elif attempts_available == 1:
        print("""
        ...... 🦅💨
    🐍🆘""")
    else:
        print("""
      💥🦅
    🐍😱""")


def play_game(mystery_word):
    #updates variables, validates guesses, checks if player wins/loses
    mystery_word_display = "_" * len(mystery_word)
    indices_of_letters_that_match_guess = [] # used to replace "_" with correct letters
    game_over = False
    letters_guessed = []
    attempts_available = 7
    print_emoji_status(attempts_available)
    
    while not game_over and attempts_available > 0:
        print()
        print ("Please guess a letter.")
        guess = input("> ").upper()
        print()
        if len(guess) == 1 and guess.isalpha(): # has to be one letter long and an alphabetical letter
            if guess in letters_guessed:
                print("You've already guessed ", guess, ". Try again!")
            elif guess in mystery_word:
                letters_guessed.append(guess)
                attempts_available = attempts_available - 1 # move to a function with above line?
                print("Yippie! 🐍")
                print(guess,"is in the mystery word!")
                print()

                mystery_word_list = list(mystery_word_display) # makes mystery_word_status_display a list
                
                # indices_of_letters_that_match_guess = [i for i, letter in enumerate(mystery_word) if letter == guess]
                #     # if letter in guess matches with a letter in the mystery_word, make a list of the index that letter
                #     # allows us to have a "new" list after each iteration, hence avoiding the bugs associated with append
                
                # for index in indices_of_letters_that_match_guess:
                #     mystery_word_list[index] = guess # replaces the _ with the letter guessed 
                
                # mystery_word_display = "".join(mystery_word_list) # would have been nice to print them spaced out

                """ this apparently works~!"""
                for i, letter in enumerate(mystery_word):
                    if letter == guess:
                        mystery_word_list[i] = guess
                        mystery_word_display = "".join(mystery_word_list)

                if "_" not in mystery_word_display:
                    game_over = True

            else: #if guess not in mystery_word
                letters_guessed.append(guess)
                attempts_available = attempts_available - 1
                print("Muhaha... 🦅 ")
                print()
                print("Incorrect guess❗️", guess,"is not in the word.")

        else: #if they don't input a single letter or an alphabetical letter
            print("Invalid entry. Please try again!")
        
        print_emoji_status(attempts_available)
        print()
        print("Mystery Word:", mystery_word_display, "🔍")
        
    if game_over: #once game_over = True 
        print("""Congrats, you found the mystery word! 🎉 
PEPINO IS SAFE! 💕 🐍""")
    else:
        print("""Oh no! 😭 BENITO flew away with PEPINO. 🦅 
The mystery word was: """, mystery_word,"!")
    print()
    
def replay_game():
    # asks user if they want to play again or exit the program
    while True:
        choice = input("Would you like to play again? Enter 'Y' for yes and 'N' for no.").lower()
        if choice == "y":
            print()
            print("Awesome! Good luck. 🤗")
            start_hangman()
        elif choice == "n":
            print("Goodbye!")
            break
        else:
            print("Please enter Y or N.")

    """Bug: after winning more than twice in a row, it will not recognize a N input and ask the user again."""

def start_hangman():
    # houses the functions that run the game
    mystery_word = picking_mystery_word()
    introducing_game()
    play_game(mystery_word)
    replay_game()

start_hangman()


# NICE TO HAVE's:
""" 
# > Player can guess the entire word 
# > Player can choose level of difficulty which changes how many attempts they have available to them
# > Player can choose a theme for the mystery words they are guessing. Each theme pulls up a different list of mystery words.
# > Use colorama library to customize the color of the text
# > Use time library to edit how fast/slow specific code is executed
# > Personalize the game more by asking for their name
# > If sounds can be played from terminal, add sounds """


