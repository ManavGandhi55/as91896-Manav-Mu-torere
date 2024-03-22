'''Mū tōrere is a Moari board game played on an octagon shaped board, which has 9 spots 
to place the stones on, one on each corner of the octagon called periperi and lines 
connecting it to the center which is called the Putahi, which is the 9th spot. In order 
to win you have to try and block the opposing player from being able to make a name'''

import os
import time

#imports the os module for python.

spots = {
    1: "B",
    2: "B",
    3: "B",
    4: "B",
    5: "R",
    6: "R",
    7: "R",
    8: "R",
    9: "0"
}
# The dictionary above stores the starting positions of the Perpere on the board.

sec_spots = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
#This list stores the spots that are available to be played on.


def main_board():
    print('\n    ' + spots[8] + '8  --  ' + spots[1] + '1   ')
    print('   \\          /')
    print('  ' + spots[7] + '7          ' + spots[2] + '2')
    print('  --    ' + spots[9] + '9    --')
    print('  ' + spots[6] + '6          ' + spots[3] + '3   ')
    print('   /          \\')
    print('    ' + spots[5] + '5  --  ' + spots[4] + '4   ')


#This function prints the main board.


def second_board():
    print('\n     ' + sec_spots[7] + '  -  ' + sec_spots[0] + '   ')
    print('    \\       /')
    print('   ' + sec_spots[6] + '         ' + sec_spots[1] + '')
    print('   -    ' + sec_spots[8] + '    -')
    print('   ' + sec_spots[5] + '         ' + sec_spots[2] + '   ')
    print('    /       \\')
    print('     ' + sec_spots[4] + '  -  ' + sec_spots[3] + '   ')


#This function prints the second board which holds the spots that are available.

current_player = 0
#This variable stores the current player.

players = {1: "B", 2: "R"}
#This dictionary stores the players and to there perepere colour.

quit = False
playing = True
#boolean variables for the while loop.

name_list = []
#empty lists for playermoves and namelist before the while loop starts

can_move = 0

def moved_piece():
    

def introduction():
    print("Welcome to my Mū tōrere game, made my Manav Gandhi")

    name_list = []
    player1 = input("Player 1, please enter your name: ")
    player2 = input("Player 2, please enter your name: ")
    name_list.append(player1)
    name_list.append(player2)
    #This is a part of code which asks the players for their playernames
    #modifies namelist to include the names of the players.
    if len(name_list) == 2:
        print("Welcome", name_list[0], "and", name_list[1],
              "to the traditional Maori game, Mū tōrere!")
        #This introduces the game to the players, including their playername variables
    else:
        print("Please enter a valid name for player 1 and 2")
        #This if else statement checks if there are 2 player names inputted into the code.
        #and if not, it asks the user to enter a valid name for player 1 and 2.
    rules_check = input("Do you know the rules of Mu torere: ").lower()
    if rules_check == "yes":
        print("Okay lets get started then...")
    else:
        print("The rules to Mu torere are very simple...")
        print(
            "The game is played on an 8-sided board, with 9 spots to place the Perepers's on as the spot in the middle (the putahi) is the 9th spot. Each player takes turns moving to an unoccupied spot on the board. Two players cannot occupy the same spot at the same time. In order to win, you need to block the opposing player from being able to move."
        )
        #This is the rules of the game, which it asks the player if they already know them or not.
        rules_finish = input("Are you finished reading the rules?: ").lower()
        if rules_finish == "yes":
            print("Okay lets get started then...")
        else:
            print("Well you'll figure it out along the way...")
        #Asks if they're finished reading the rules to Mu torere.
    print("The game will now begin...")


while playing is True:

    os.system('cls' if os.name == 'nt' else 'clear')
    #clears screen to remove excessive clutter

    introduction()

    main_board()
    #prints main board

    second_board()
    #prints second board
    if current_player == 0:
        move = input("Player 1, please enter the number of the spot you would like to move to: ")
        if move == "quit":
            print("Oh, I see how it is, you're quitting... You know quitters are the weakest form of homosapiens.")
            
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            move = int(move)
            #asks player 1 to enter their move.
            if spots[move] == players[1] or spots[move] == players[2]:
                can_move = False 
            else:
                can_move = True
                
            if can_move is True:
                
                spots[move] = players[1]
                main_board()
            else:
                print("You cannot move there, please try again.")
                move = input("Player 1, please enter the number of the spot you would like to move to: ")
    elif current_player == 1:
        
