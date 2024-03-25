'''Mū tōrere is a Moari board game played on an octagon shaped board, which has 9 spots 
to place the stones on, one on each corner of the octagon called periperi and lines 
connecting it to the center which is called the Putahi, which is the 9th spot. In order 
to win you have to try and block the opposing player from being able to make a name'''

import os
import time

#imports the os module for python.

spots = {
    1: "R",
    2: "R",
    3: "R",
    4: "R",
    5: "B",
    6: "B",
    7: "B",
    8: "B",
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

players = {1: "B", 2: "R"}
#This dictionary stores the players and to there perepere colour.

turn = 1
#This variable stores the current turn.

win = False
#boolean variables for the while loop.

name_list = []
player_moves = []

#empty lists for playermoves and namelist before the while loop starts

player_move = 0
can_move = 0
#variables for the while loop.

delay_one = 1


def rules():
    print("The rules to Mu torere are very simple...")
    time.sleep(delay_one)
    print("The game is played on an 8-sided board.")
    time.sleep(1.5)
    print(
        "with 9 spots to place the Perepers's on as the spot in the middle (the putahi) is the 9th spot. "
    )
    time.sleep(3)
    print(
        "Each player takes turns moving to an unoccupied spot on the board. ")
    time.sleep(2.5)
    print("Two players cannot occupy the same spot at the same time.")
    time.sleep(2)
    print(
        "In order to win, you need to block the opposing player from being able to move."
    )
    time.sleep(3)
    # This is the rules of the game, which it asks the player if they already know them or not.
    rules_finish = input(
        "Are you finished reading the rules?(Yes/No): ").lower()
    if rules_finish == "yes":
        print("Okay let's get started then...")
        time.sleep(delay_one)
    elif rules_finish == "no":
        print("Well you'll figure it out along the way...")
        time.sleep(delay_one)
    else:
        print("Well you'll figure it out along the way...")
        time.sleep(delay_one)
    # Asks if they're finished reading the rules to Mu torere.


def introduction():
    print("Welcome to my Mū tōrere game, made by Manav Gandhi")
    player1 = input("Player 1, please enter your name: ")
    print(player1 + " you are the Blue Perepere.")
    time.sleep(delay_one)
    player2 = input("Player 2, please enter your name: ")
    print(player2 + " you are the Red Perepere.")
    time.sleep(delay_one)
    name_list.append(player1)
    name_list.append(player2)
    # This is a part of code which asks the players for their playernames
    # Modifies name_list to include the names of the players.
    print("Welcome", name_list[0], "and", name_list[1],
          "to the traditional Maori game, Mū tōrere!")
    # This introduces the game to the players, including their playername variables
    rules_check = input("Do you know the rules of Mu torere(Yes/No): ").lower()
    if rules_check == "yes":
        print("Okay let's get started then...")
        time.sleep(delay_one)
    elif rules_check == "no":
        rules()
        #rules function
    else:
        print("I'll take that as a yes...")
    print("The game will now begin...")
    time.sleep(delay_one)
    return name_list
    #returns the name_list to the main code, useful in the while loop.


def move_logic():
    global player_moves
    #global variable for player_moves
    player_move = int(
        input(
            f"{name_list[turn - 1]} ({players[turn]}) What piece would you like to move?"
        ))
    #This asks the player what piece they would like to move.
    player_moves.append(player_move)
    #This adds the player's move to the player_moves list.
    new_position = moved_piece(player_move, spots)
    #This calls the moved_piece function to move the piece.
    if new_position is not None:
        spots[new_position] = players[turn]
        spots[player_move] = "0"
    else:
        print(f"Invalid move {name_list[turn - 1]}. This is your last try")
        time.sleep(delay_one)
        player_move = int(
            input((name_list[turn - 1], "(", players[turn],
                   ") What piece would you like to move?")))
    #This checks if the move is valid and if it is, it moves the piece, else error msg


def moved_piece(player_move, spots):
    #This function checks if the player's move is valid and if it is, it returns the value
    connecting_spots = {
        1: [8, 2, 9],
        8: [7, 1, 9],
    }
    # This dictionary stores the spots that are on the neighbouring sides of the connecting spots.

    if player_move in connecting_spots:
        available_spots = connecting_spots[player_move]
        for spot in available_spots:
            if spots[spot] == '0':
                return spot
    # This checks if the player's move is on a connecting spot.
    elif player_move == 9:
        for zero in spots:
            if spots[zero] == '0':
                return zero
    # This checks if the player's move is on the putahi. If it is, it returns the spot that
    else:
        if player_move - 1 in spots and spots[player_move - 1] == '0':
            return player_move - 1
        elif player_move + 1 in spots and spots[player_move + 1] == '0':
            return player_move + 1
        elif spots[9] == '0':
            return 9
        #This checks if the player's move is valid on its neighbouring sides

        else:
            return None


# Start of game
name_list = introduction()
# This calls the introduction function and stores the player names in name_list.
while not win:
    os.system('cls' if os.name == 'nt' else 'clear')
    # clears screen to remove excessive clutter
    main_board()
    # prints main board
    second_board()
    # prints second board
    move_logic()
    # Handle player move

    turn = 2 if turn == 1 else 1
    # Switch player turn
