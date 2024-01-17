'''
This program is a simple word-guessing game that takes a word from a predefined list and asks the user to guess the secret word,
the program displays the user's progress through displaying the missed guesses made by the user 
and also displays the length of the secret word with a string of underscores which updates the underscores to reflect the user's guess of the secret word.
The program terminates after the user has correctly guessed the secret word and displays the total number of guesses the user took to get to the secret word
as well as the correct word.
This program takes user input that is not case sensitive and allows the user to type in lower and upper case letters as acceptable inputs to guess the word.
'''

#Imports to choose secret word from predefined list.
import random

#This function uses the random module to pick a random word from a list and returns the secret word.
def get_secret(word_bank):
    secret_word = random.choice(word_bank)
    return secret_word

#This function tracks the user's progress and asks for the user's next guess, the function continues asking the user for input until correct input is entered.
def display_guess(display_str, misses):
    print("Missed:", misses, "times \tWord:", display_str)
    while True:
        new_guess = input("Guess a letter: ")
        if len(new_guess) == 1 and new_guess.isalpha():
            break
        print("Invalid input, please enter a single letter!")
    print()

    #The .upper() method call is used so that case sensitivity is not an issue.
    return new_guess.upper()

#This function checks if the user's guess is in the secret word and updates the display string to reflect the secret word.
#Note index positions are incremented by two because of the space between the underscores to display the string.
def new_display_string(secret_word, display_str, guess):
    if guess in secret_word:
        index = 0

        #This line changes the display of the string into a list because we want to index only the positions
        #where the user's guess has the same character as the secret word.
        display_str = list(display_str)
        
        #This for loop loops through the secret word as a list and we apply conditionals to check if the user's guess is the same as the character in
        #the secret word, if it is, then we change the character at the index position to reflect the user's guess.
        for char in list(secret_word):
            if guess == char:
                display_str[index] = guess
            index += 2
        
        #Since we initially changed the display string to a list, we want to change the display string back to a string with the .join() method call.
        #The empty quotes imply that we do not want anything between the string.
        return "".join(display_str)
    
    #If the user's guess is not in the secret word, we want to leave the display string unchanged.
    return display_str

#This function runs the word guessing game.
def main():
    #This is the word bank that the game can choose from
    word_list = ['apple','alias','alloy','banana','bongo','bogey','category','chains','quest','bubble','clothes','basket','guitar']
    new_word_list = []

    #This for loop changes the items in the word list to upper case to display the secret word.
    for word in word_list:
        new_word_list.append(word.upper())

    #These two variables track the guesses made by the user.
    total_guesses = 0
    missed_guesses = 0

    #This variable gets a random word from the list of upper case words and the next variable displays the length of the secret word in underscores.
    secret = get_secret(new_word_list)
    display_string = "_ " * len(secret)

    print("Welcome to ...")
    print('''
    ██████╗ ██╗   ██╗███████╗███████╗███████╗██╗███╗   ██╗ ██████╗      ██████╗  █████╗ ███╗   ███╗███████╗
    ██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝██║████╗  ██║██╔════╝     ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
    ██║  ███╗██║   ██║█████╗  ███████╗███████╗██║██╔██╗ ██║██║  ███╗    ██║  ███╗███████║██╔████╔██║█████╗  
    ██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║██║██║╚██╗██║██║   ██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
    ╚██████╔╝╚██████╔╝███████╗███████║███████║██║██║ ╚████║╚██████╔╝    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
    ''')
    print("Getting word ...\n\n\n")

    while True:

        #Asks the user to guess a letter of the secret word
        user_guess = display_guess(display_string, missed_guesses)

        #Updates the display string to reflect the result of the user's guess
        display_string = new_display_string(secret, display_string, user_guess)

        #Check user's guess if their guess was in the secret or not and keeps tracks of their total and missed guesses
        if user_guess not in secret:
            missed_guesses += 1
        total_guesses += 1

        #If the user has correctly guessed the secret word, the while loop is exited.
        if display_string.replace(" ","") == secret:
            break

    #Display a summary of what the secret word is and total number of guesses made by the user.
    print("Correct! The word was", secret)
    print("Solved using", total_guesses, "guesses")

main()
