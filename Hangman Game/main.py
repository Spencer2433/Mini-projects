#A program to play the hangman game

# import random to used to randomly choose an item from a list 
# import time to import the actual time from your pc to use in the program
# import os to clear the screen
import random
import time
import os

#Initial steps to invite in the game
print(f"\n Welcome to Hangman by Spencer Moriasi\n")
name = input("What is your name: ")
os.system("cls")
print(name, f"welcome to my world!")
time.sleep(1)
print(f"\nEnjoy it!")
time.sleep(1)
print(f"\nThe game is about to start")
time.sleep(3)

os.system("cls")


# The main function initializes our count, display, word, already_guessed, length and play_game
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game

    # Contains the Hangman words player has to guess
    word_to_guess = ["helicopter", "player", "random", "rainpour", "choice"] 
    # The random module helps us choose a random word from word_to_guess
    word = random.choice(word_to_guess)
    # Helps us get length of the string 
    length = len(word)
    count = 0
    # Draws a line for us proportianal to length of the word
    display = '_' * length
    # This would contain the string indices of the correctly guessed words
    already_guessed = []
    play_game = ""


# A loop to re-execute the program after the first round.
def play_loop():
    # play_game is used to either continue the game after its played once or end it according to the user
    global play_game
    play_game = input(f"Do you want to play again? \n 'Y' = 'yes' \n 'N' = 'no'\n" )
    
    while play_game not in ["y", "Y", "yes", "Yes", "YES", "n" , "N", "no", "No", "NO"]:
        play_game = input(f"Do you want to play again? \n 'Y' = 'yes' 'N' = 'no'\n" )
    if play_game in ["y", "Y", "yes", "Yes", "YES"]:
        # Main function is called to initialize the variables again and to pick another random word
        main()
        hangman()
    elif play_game in ["n" , "N", "no", "No", "NO"]:
        print(f"Thank you for playing.")
        exit()

# Initializing all conditions required for the game.
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    # Maximum number of guesses allowed to the user for each word
    limit = 5 
    # Takes the input from the user for the guessed word
    guess = input(f"This is the Hangman Word: " + display + f"\nEnter your guess: \n")
    # To remove the user provided letter from the random word
    # Everything is stripped apart from the 'guess'
    guess = guess.strip()
    
    # If loop to check if guess was not one letter or was a number then calls hangman again
    if len(guess.strip()) != 1 or guess <= "9":
        print("Invalid input. Try a letter.")
        hangman()

    # If the letter is correctly guessed, search for it in the word via index searches    
    elif guess in word:
        #add the guessed word in the already_guessed list by extending
        already_guessed.extend(guess)
        # Finding index position of the guessed letter using find method
        index = word.find(guess)
        # Finding the guessed letter position in the word
        # Prints the letters till it gets to the guess, prints an underscore, then coninues printing the words
        word = word[:index] + "_" + word[index + 1 :]
        # Filling the guessed letter in the word
        # Prints the underscores till it gets to the guess, prints the guess, then continues printing underscores
        display = display[:index] + guess + display[index + 1:]
        print(display + '\n')

    # If the guessed letter was already correctly guessed before
    elif guess in already_guessed:
        print(f"Try another letter")

    # If the user inputs the wrong letter then count inreases and hangman appears
    # The user is also reminded of the number of tries remaining
    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("  _____   \n"
                  " |        \n"
                  " |        \n"
                  " |        \n"
                  " |        \n"
                  " |        \n"
                  " |        \n"
                  " |        \n"
                  "_|_")
            print(f"Wrong guess." + str(limit - count) + f" tries remaining\n")

        if count == 2:
            time.sleep(1)
            print("  _____   \n"
                  " |     |  \n"
                  " |     |  \n"
                  " |        \n"
                  " |        \n"
                  " |        \n"
                  " |        \n"
                  " |        \n"
                  "_|_")
            print(f"Wrong guess." + str(limit - count) + f" tries remaining\n")    

        if count == 3:
            time.sleep(1)
            print("  _____   \n"
                  " |     |  \n"
                  " |     |  \n"
                  " |     O  \n"
                  " |        \n"
                  " |        \n"
                  " |        \n"
                  " |        \n"
                  "_|_")
            print(f"Wrong guess." + str(limit - count) + f" tries remaining\n")
            
        if count == 4:
            time.sleep(1)
            print("  _____   \n"
                  " |     |  \n"
                  " |     |  \n"
                  " |     O  \n"
                  " |    /|\ \n"
                  " |        \n"
                  " |        \n"
                  " |        \n"
                  "_|_")
            print(f"Wrong guess." + str(limit - count) + f" tries remaining\n")

        if count == 5:
            time.sleep(1)
            print("  _____   \n"
                  " |     |  \n"
                  " |     |  \n"
                  " |     O  \n"
                  " |    /|\ \n"
                  " |     |  \n"
                  " |    / \ \n"
                  " |        \n"
                  "_|_")
            print(f"Wrong guess. You are hanged!!")
            # The user is shown his guess
            print(f"You guessed:", already_guessed)
            print(f"The remaining part:", word)
            play_loop()
    
    # Since we are removing letters from word, we win if word is left with all blanks
    if word == '_' * length:
        print("Congratulations! You have guessed the word correctly")
        play_loop()

    # If the count is not equal to the limit, run hangman function again
    # The values will not be initialized since the are initialized in the main function    
    elif count != limit:
        hangman()

main()

hangman()
