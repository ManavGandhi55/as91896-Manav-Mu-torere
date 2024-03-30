'''Mū tōrere is a Moari board game played on an octagon shaped board, which has 9 spots 
to place the stones on, one on each corner of the octagon called periperi and lines 
connecting it to the center which is called the Putahi, which is the 9th spot. In order 
to win you have to try and block the opposing player from being able to make a name'''

import os
import time
from termcolor import colored, cprint

#imports the os module for python.

players = {1: "B", 2: "R"}

#This dictionary stores the players and to there perepere colour.

p1_colour = "blue"
#player 1 colour
p2_colour = "red"
#player 2 colour
error_colour = "yellow"
#error colour



exit_list = [
    "quit", "break", "lobby", "exit", "leave", "end", "stop", "end game",
    "terminate", "abort", "halt", "finish", "close", "done", "escape", "off",
    "out", "end session"
]
#This list stores the commands that the user can use to exit the game.

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

spots = {
    1: colored("R", p2_colour),
    2: colored("R", p2_colour),
    3: colored("R", p2_colour),
    4: colored("R", p2_colour),
    5: colored("B", p1_colour),
    6: colored("B", p1_colour),
    7: colored("B", p1_colour),
    8: colored("B", p1_colour),
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


def exit_game(player_move):
    if player_move.lower() in [item.lower() for item in exit_list]:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Thank you for playing Mū Tōrere!")
        time.sleep(delay_one)
        os.system('cls' if os.name == 'nt' else 'clear')
        return True
    else:
        return False
    #This function checks if the player wants to quit the game, if so it clears the screen and prints a message.


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
    name_list.append(input("Player 1, please enter your name: "))
    #This asks for the name of the first player, appending it to a list.
    print(name_list[0] + " you are the Blue Perepere.")
    time.sleep(delay_one)
    name_list.append(input("Player 2, please enter your name: "))
    #This asks for the name of the second player, appending it to a list.
    print(name_list[1] + " you are the Red Perepere.")
    time.sleep(delay_one)
    # This is a part of code which asks the players for their playernames

    print("Welcome", name_list[0], "and", name_list[1],
          "to the traditional Maori game, Mū tōrere!")
    # This introduces the game to the players, including their playername variables
    rules_check = input("Do you know the rules of Mu torere(Yes/No): ").lower()
    # This asks if the players know the rules of the game.
    if rules_check == "yes":
        print("Okay let's get started then...")
        time.sleep(delay_one)
    elif rules_check == "no":
        rules()
        #rules function
    else:
        print("I'll take that as a yes...")
        time.sleep(delay_one)
    return name_list
    #returns the name_list to the main code, useful in the while loop.


def move_logic(player_moves, turn):
    while True:
        #This while loop is for the player to move.
        player_move = input(
            f"{name_list[turn - 1]} ({players[turn]}) What piece would you like to move? "
        )
        #This asks the player what piece they want to move.
        if exit_game(player_move):
            return True  # Exit the game

        try:
            #This try statement is for the player to move.
            player_move = int(player_move)
            #This converts the player_move variable to an integer.
            if 1 <= player_move <= 9 and spots[player_move] == players[turn]:
                #This checks if the player_move is a valid move and if the spot is occupied by the player's pereper
                new_position = moved_piece(player_move, spots)
                #This calls the moved_piece function to get the new position of the piece.
                if new_position is not None:
                    #This checks if the new position is not None.
                    spots[new_position] = players[turn]
                    #This updates the spots dictionary with the new position.
                    spots[player_move] = "0"
                    #This updates the spots dictionary with the old position as 0.
                    player_moves.append(player_move)
                    # Add the move to player_moves
                    return False
                    # Valid move, continue the game

                else:
                    #This is for if the new position is None.
                    cprint(f"Invalid move {name_list[turn - 1]}. Please try again.", error_colour)
                    time.sleep(delay_one)
                    continue
                    #Prints the error message, then sends back to the top of the while loop
            else:
                cprint(f"Invalid move {name_list[turn - 1]}. Please try again.", error_colour)
                time.sleep(delay_one)
                continue
                #Prints the error message, then sends back to the top of the while loop
        except ValueError:
            #This is for if the player_move is not a valid integer.
            cprint(f"Invalid move {name_list[turn - 1]}. Please try again.", error_colour)
            time.sleep(delay_one)
            continue
            #Prints the error message, then sends back to the top of the while loop


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
            if player_move == 1:
                if spots[8] == players[turn] and spots[2] == players[turn]:
                    return None
                else:
                    if spots[spot] == '0':
                        return spot
            elif player_move == 8:
                if spots[7] == players[turn] and spots[1] == players[turn]:
                    return None
                else:
                    if spots[spot] == '0':
                        return spot
            #This part of the code checks if its own pieces or on either side of the connecting pieces.
            else:
                return None
    # This checks if the player's move is on a connecting spot.
    elif player_move == 9:
        for zero in spots:
            if spots[zero] == '0':
                return zero
    # This checks if the player's move is on the putahi. If it is, it returns the spot.

    else:
        if spots[player_move -
                 1] == players[turn] and spots[player_move +
                                               1] == players[turn]:
            return None
        # This is a boundray to check if the player has its own pieces on either side of it.
        if player_move - 1 in spots and spots[player_move - 1] == '0':
            return player_move - 1
        elif player_move + 1 in spots and spots[player_move + 1] == '0':
            return player_move + 1
        elif spots[9] == '0':
            return 9
        else:
            return None
    #This checks if the player's move is valid on its neighbouring sides.


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
    if move_logic(player_moves, turn) is True:
        break
    # Handle player move

    turn += 1
    if turn > 2:
        turn = 1
    # Switch player turn
