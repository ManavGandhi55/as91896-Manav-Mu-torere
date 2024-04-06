'''Mū tōrere is a Moari board game played on an octagon shaped board, which has 9 spots 
to place the stones on, one on each corner of the octagon called periperi and lines 
connecting it to the center which is called the Putahi, which is the 9th spot. In order 
to win you have to try and block the opposing player from being able to make a name'''

import os
# imports the os module for Python
import time
# imports the time module for Python
from termcolor import colored, cprint
# imports the termcolor module for Python

cpu_colour = "green"
# This is the colour that is used for cprint functions(no inputs)
p1_colour = "blue"
# This is player 1 colour.
p2_colour = "red"
# This is player 2 colour.
error_colour = "yellow"
# This is the colour that is used for error messages.
# These are the colour variables that are used for the text in the game.

color_mapping = {"B": p1_colour, "R": p2_colour}
# This dictionary maps the player's colour to the player's colour.

players = {1: "B", 2: "R"}
# This dictionary stores the players' colours.
# This can be changed in the future to allow for different reason like Moari names of blue and red.

player_1_color = color_mapping[players[1]]
# This will give you "blue"

player_2_color = color_mapping[players[2]]
# This will give you "red"

#This dictionary stores the players and to there perepere colour.

exit_list = [
    "quit", "break", "lobby", "exit", "leave", "end", "stop", "end game"
]
# This list stores the commands that the user can use to exit the game.

turn = 1
# This variable stores the current turn.

win = False
# boolean variables for the while loop.

name_list = []
player_moves = []
# empty lists for playermoves and namelist before the while loop starts

player_move = 0
can_move = 0
# variables for the while loop.

delay_one = 1
# This is the default delay for the game.

spots = {
    1: colored(players[2], player_2_color),
    2: colored(players[2], player_2_color),
    3: colored(players[2], player_2_color),
    4: colored(players[2], player_2_color),
    5: colored(players[1], player_1_color),
    6: colored(players[1], player_1_color),
    7: colored(players[1], player_1_color),
    8: colored(players[1], player_1_color),
    9: "0"
}
# The dictionary above stores the starting positions of the Perpere on the board.
# The dictionary stores the coloured perepere and the singular empty space.
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


# This function prints the main board.


def second_board():
    print('\n     ' + sec_spots[7] + '  -  ' + sec_spots[0] + '   ')
    print('    \\       /')
    print('   ' + sec_spots[6] + '         ' + sec_spots[1] + '')
    print('   -    ' + sec_spots[8] + '    -')
    print('   ' + sec_spots[5] + '         ' + sec_spots[2] + '   ')
    print('    /       \\')
    print('     ' + sec_spots[4] + '  -  ' + sec_spots[3] + '   ')


# This function prints the second board.


def exit_game(player_move):
    if player_move.lower() in [item.lower() for item in exit_list]:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Thank you for playing Mū Tōrere!")
        time.sleep(delay_one)
        os.system('cls' if os.name == 'nt' else 'clear')
        return True
    else:
        return False
    # This function checks if the player wants to quit the game, if so it clears the screen and prints a message.


def rules():
    # This function prints the rules of the game.
    cprint("The rules to Mu torere are very simple...", cpu_colour)
    time.sleep(delay_one)
    cprint("The game is played on an 8-sided board.", cpu_colour)
    time.sleep(1.5)
    cprint(
        "with 9 spots to place the Perepers's on as the spot in the middle (the putahi) is the 9th spot. ",
        cpu_colour)
    time.sleep(3)
    cprint(
        "Each player takes turns moving to an unoccupied spot on the board. ",
        cpu_colour)
    time.sleep(2.5)
    cprint("Two players cannot occupy the same spot at the same time.",
           cpu_colour)
    time.sleep(2)
    cprint(
        "In order to win, you need to block the opposing player from being able to move.",
        cpu_colour)
    time.sleep(3)
    # This is the rules of the game, which it asks the player if they already know them or not.
    rules_finish = input(
        "Are you finished reading the rules?(Yes/No): ").lower()
    if rules_finish == "yes":
        cprint("Okay let's get started then...", cpu_colour)
        time.sleep(delay_one)
    elif rules_finish == "no":
        cprint("Well you'll figure it out along the way...", cpu_colour)
        time.sleep(delay_one)
    else:
        cprint("Well you'll figure it out along the way...", cpu_colour)
        time.sleep(delay_one)
    # This asks the player if they are finished reading the rules or not.


def introduction():
    cprint("Welcome to my Mū tōrere game, made by Manav Gandhi!", cpu_colour)
    name_list.append(input("Player 1, please enter your name: "))
    #This asks for the name of the first player, appending it to a list.
    cprint(name_list[0] + " you are the Blue Perepere.", p1_colour)
    time.sleep(delay_one)
    name_list.append(input("Player 2, please enter your name: "))
    #This asks for the name of the second player, appending it to a list.
    cprint(name_list[1] + " you are the Red Perepere.", p2_colour)
    time.sleep(delay_one)
    # This is a part of code which asks the players for their playernames
    # It then modifies the empty name_list list to store the playernames.

    cprint("Welcome " + name_list[0] + " and " + name_list[1] +
           " to the traditional Maori game, Mū tōrere!",
           color=cpu_colour)

    # This introduces the game to the players, including their playername variables
    rules_check = input("Do you know the rules of Mu torere(Yes/No): ").lower()
    # This asks if the players know the rules of the game.
    if rules_check == "yes":
        print("Okay let's get started then...")
        time.sleep(delay_one)
    elif rules_check == "no":
        rules()
        # rules function
    else:
        print("I'll take that as a yes...")
        time.sleep(delay_one)
    return name_list


    # returns the name_list to the main code, useful in the while loop.
def move_logic(player_moves, turn):
    while True:
        player_move = input(
            f"{name_list[turn - 1]} ({players[turn]}) What piece would you like to move? "
        )
        # This asks the player what piece they want to move.
        if exit_game(player_move):
            return True
            # Exit the game

        try:
            player_move = int(player_move)
            # This trys makeing the player move and integer.
            if 1 <= player_move <= 9 and spots[player_move] == colored(
                    players[turn], color_mapping[players[turn]]):
                # This checks if the player move is a number between 1 and 9
                # and if the player move is the same as the players colour.
                new_position = moved_piece(player_move, spots)
                # This calls the moved_piece function.
                if new_position is not None:
                    spots[new_position] = colored(players[turn],
                                                  color_mapping[players[turn]])
                    spots[player_move] = "0"
                    player_moves.append(player_move)
                    # This moves the piece to the new position and replaces the old position with a 0.
                    return False
                    # This returns false to the main code.
                else:
                    cprint(
                        f"Invalid move {name_list[turn - 1]}. Please try again.",
                        error_colour)
                    time.sleep(delay_one)
                    continue
            else:
                cprint(
                    f"Invalid move {name_list[turn - 1]}. Please try again.",
                    error_colour)
                time.sleep(delay_one)
                continue
                # This prints an error message and asks the player to try again.
        except ValueError:
            cprint(f"Invalid move {name_list[turn - 1]}. Please try again.",
                   error_colour)
            time.sleep(delay_one)
            continue
            # This prints an error message and asks the player to try again.


def moved_piece(player_move, spots):
    # This function checks if the player's move is valid and if it is, it returns the value
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
    # This checks if the player's move is on the neighbouring sides of the connecting spots.
                else:
                    if spots[spot] == '0':
                        return spot
                    #This part of the code checks if its own pieces or on either side of the connecting pieces.
            elif player_move == 8:
                if spots[7] == players[turn] and spots[1] == players[turn]:
                    return None
                    #This part of the code checks if its own pieces or on either side of the connecting pieces.
                else:
                    if spots[spot] == '0':
                        return spot
            else:
                return None
                # This checks if the player's move is on a connecting spot.
    elif player_move == 9:
        for zero in spots:
            if spots[zero] == '0':
                return zero
                # This checks if the player's move is on the putahi. If it is, it returns the spot.
    else:
        if spots[player_move - 1] == colored(players[turn], color_mapping[
                players[turn]]) and spots[player_move + 1] == colored(
                    players[turn], color_mapping[players[turn]]):
            # This is a boundray to check if the player has its own pieces on either side of it.
            return None
        if player_move - 1 in spots and spots[player_move - 1] == '0':
            return player_move - 1
            # This checks it the neighbouring peice is empty. If it is, it returns the spot.
        elif player_move + 1 in spots and spots[player_move + 1] == '0':
            return player_move + 1
            # This checks it the neighbouring peice is empty. If it is, it returns the spot.
        elif spots[9] == '0':
            return 9
            # This checks if the player's move is on the putahi. If it is, it returns the spot.
        else:
            return None


def winning_logic(spots):
    global win
    for key, value in spots.items():
        if value == '0':
            empty_spot = key
            if empty_spot == 1:
                if (spots.get(8) == players.get(turn, "") and 
                    spots.get(2) == players.get(turn, "") and 
                    spots.get(9) == players.get(turn,  "")):
                    win = True
                    print("true")
                    time.sleep(3)
                else:
                    win = False
                    print("false")
                    time.sleep(3)
    
            elif empty_spot == 8:
                if (spots.get(7) == players.get(turn, "") and 
                    spots.get(1) == players.get(turn, "") and 
                    spots.get(9) == players.get(turn, "")):
                    win = True
                    print("true")
                    time.sleep(3)
                else:
                    win = False
                    print("false")
                    time.sleep(3)
            elif (spots.get(empty_spot + 1) == players.get(turn, "") and 
                  spots.get(empty_spot - 1) == players.get(turn, "") and 
                  spots.get(9) == players.get(turn, "")):
                win = True
                print("true")
                time.sleep(3)
            else:
                win = False
                print("false")
                time.sleep(3)

    return win




# This checks if the player's move is valid on its neighbouring sides.

# Start of game
name_list = introduction()
# This calls the introduction function and stores the player names in name_list.
while not win:
    # gameloop

    os.system('cls' if os.name == 'nt' else 'clear')
    # clears screen to remove excessive clutter

    main_board()
    # prints main board

    second_board()
    # prints second board
    winning_logic(spots)
    if win:
        cprint("Congratulations " + name_list[turn - 1] + " wins!", cpu_colour)
        break
    # checks if the player has won

    if move_logic(player_moves, turn) is True:
        break
        # Handle player move

    turn += 1
    if turn > 2:
        turn = 1
    # Switch player turn
