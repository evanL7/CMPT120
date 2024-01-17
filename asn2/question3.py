'''
This program has the user choose a unit (Witch, Orgre, Robber) to play against the computer and tracks the number of wins for both the computer and the user.
'''
#Imports to randomly choose from the list of units to assign to the computer's choice
import random

#This function chooses the computer's unit from the army of ogres, robbers, and witches.
def computer_choice(army_units):
    computer_pick = random.choice(army_units)
    return computer_pick

#This function takes in input from the user and continues to ask until acceptable input is received.
def gameplay_display(computer_unit,army_list,army_units):
    
    while True:
        #Ask user which unit they want to play
        player_choice = input("Choose (w)itch, (o)gre, (r)obber: ")
        
        #The method call .lower() is used so that case sensitivity is not an issue.
        player_choice = player_choice.lower()

        #Since we expect the user to input a single letter, we ensure that the input is correct and the variable army_list is a temporary variable that
        #stores a list of the first index position of the units (w)itch, (o)gre, and (r)obber.
        if len(player_choice) == 1 and player_choice in army_list:
            
            #This line finds the index of the user's choice
            index = army_list.index(player_choice)
            
            #Displays the computer's choice and the user's choice.
            print("Computer:", computer_unit)
            print("User:", army_units[index])
            break

        print("Invalid input, please enter 'w', 'o', or 'r'")
        print()
    
    #This line changes the user's input from the single letter to the full word of the unit so that the next function can evaluate whether the computer or user wins.
    player_choice = army_units[index]
    return player_choice

#This function determines who wins and if both the computer and user input identical units, returns a tie, where no one wins.
def gameplay(computer_unit,player_unit,army):
    tie = -1
    
    #This conditional returns false and implies that the computer has won by checking each winning condition.
    if (computer_unit == army[2] and player_unit == army[0]) or (computer_unit == army[1] and player_unit == army[2]) or (computer_unit == army[0] and player_unit == army[1]):
        return False
    
    #This conditional returns true and implies that the player has won by checking each winning condition.
    elif (computer_unit == army[0] and player_unit == army[2]) or (computer_unit == army[2] and player_unit == army[1]) or (computer_unit == army[1] and player_unit == army[0]):
        return True
    
    else:
        return tie

#This function asks the user if they would like to keep playing and returns their choice
def ask_play_again():
    while True:
        print()
        play_again = input("Play again  (y)es  (n)o? ")
        
        #The method call .lower() is used so that case sensitivity is not an issue.
        play_again = play_again.lower()

        if play_again == 'y' or play_again == 'n':
            #The method call .lower() is used so that case sensitivity is not an issue.
            return play_again
        print("Invalid input, please enter 'y' or 'n'")
    
#This function runs the game.
def main():
    army = ['orge','robber','witch']
    army_list = []

    #This for loop is used to evaluate the user input so that we can change the single letter to the full word of the unit.
    for units in army:
        army_list.append(units[0])

    #These variables keep track of the number of wins
    computer_wins = 0
    player_wins = 0

    print("Welcome to Witches, Ogres, and Robbers:")
    print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠞⠛⠉⠉⠛⠻⢷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠰⡍⠻⣷⣄⠀⢀⣄⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣌⡛⠷⣯⣽⣧⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡏⣀⣀⣀⠀⠀⠀⠀⢀⣀⣀⢹⣿⢿⣾⠟⠙⢿⣦⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⡄⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣼⡧⠶⠖⠚⠛⠛⠉⠉⠙⠛⠛⠲⠶⢾⣧⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣀⣤⡶⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢶⣤⣀⠀⠀⠀⠀
    ⠀⣠⣶⣿⣿⣥⣤⣤⣤⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣤⣬⣽⣿⣶⣄⠀
    ⠐⣿⣻⣿⣿⣿⡿⠀⢠⡏⠙⡟⠻⣭⣍⣙⣛⣿⣿⣛⣋⣩⣭⠟⢻⠏⢹⡆⠀⢿⣿⣿⣿⡟⣿⠃
    ⠀⠙⢿⣯⣟⡷⠦⣤⡾⢀⣤⡇⠈⠙⠯⣽⣿⡇⢸⣿⣯⠽⠋⠁⢸⡆⡀⢿⣤⠴⢾⣻⣽⡾⠋⠀
    ⠀⠀⠀⠈⠛⠛⠿⡾⢡⠏⢸⡄⠀⠀⠉⣉⣼⠁⠈⢧⣈⠉⠀⠀⢀⣇⠹⡌⢷⡿⠟⠛⠁⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⡼⣡⡟⢠⡿⣷⣄⢀⣰⣁⣭⣀⣀⣬⣈⣧⡀⣠⢾⢿⣄⢹⣌⢧⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠰⢿⡟⢠⢿⡄⠙⠓⠛⠛⠁⠀⢠⣄⠀⠈⠙⠛⠛⠋⢀⡿⡄⢻⡿⠇⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣾⣡⡎⠈⢷⣤⣀⣀⡠⠤⠚⠉⠉⠓⠦⢄⣀⣀⣤⡞⠁⠹⣌⣷⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠙⣿⢠⠂⢸⡆⠀⠹⡶⠟⠉⠁⠈⠉⠻⢶⠏⠀⢠⡇⠀⡄⣿⠋⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⢿⢰⡏⣷⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⣾⣹⣇⡿⡿⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠈⢿⠻⣿⠿⣧⡄⠀⠀⠀⠀⠀⠀⢠⣴⠿⢿⠟⢿⠃⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢳⣾⡄⠀⠀⢀⣶⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢿⣄⣠⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')

    #This variable changes depending on if the player wants to continue playing the game.
    game_on = True

    while game_on:

        #This function call is in the while loop because if the user wants to play again, we want the computer to get a new unit to play against the user.
        computer_pick = computer_choice(army)

        #This function call lets the user input their choice of unit and displays both the computer and the user's input.
        player_pick = gameplay_display(computer_pick,army_list,army)

        #This function call evaluates who wins or if there is a tie. 
        play_game = gameplay(computer_pick,player_pick,army)
        
        #These conditionals print out who wins and increments the variables that keep track of wins. 
        if play_game == True:
            print("You Win!")
            player_wins += 1
        elif play_game == -1:
            print("Tie.")        
        elif play_game == False:
            print("Computer Wins!")
            computer_wins += 1

        #Ask user if they want to play again.
        choice = ask_play_again()
        if choice == "y":
            continue
        
        #These print statements report the finals stats of the game when the user wants to quit.
        print("Computer:", computer_wins)
        print("Player:", player_wins)
        
        #This variable allows us to exit the game.
        game_on = False

    #These condtionals display who has the most wins or if the computer and user have tied.
    if player_wins > computer_wins:
        print()
        print(" " * ((len("You Win!") - len("(✧∇✧)")) //2) + "(✧∇✧)")
        print("You Win!")
    elif player_wins < computer_wins:
        print()
        print(" " * ((len("Computer Wins") - len("(╥_╥)")) //2) + "(╥_╥)")    
        print("Computer Wins")
    else:
        print()
        print("Tie.")

main()
