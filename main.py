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


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


    # This function clears the console.
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
        clear()
        print("Thank you for playing Mū Tōrere!")
        time.sleep(delay_one)
        clear()
        return True
    else:
        return False
    # This function checks if the player wants to quit the game.
    # If the player wants to quit the game, it clears the console and prints a message


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
    # This is the rules of the game, which has adequate delays between each line.

    rules_finish = input(
        "Are you finished reading the rules?(Yes/No): ").lower()
    # This asks the player if they are finished reading the rules.

    if rules_finish == "yes":
        cprint("Okay let's get started then...", cpu_colour)
        time.sleep(delay_one)
        # If yes it will print a msg, allow the player to read the msg then continue

    elif rules_finish == "no":
        cprint("Well you'll figure it out along the way...", cpu_colour)
        time.sleep(delay_one)
        # If no it will print a msg, allow the player to read the msg then continue

    else:
        cprint("Well you'll figure it out along the way...", cpu_colour)
        time.sleep(delay_one)
    # This asks the player if they are finished reading the rules or not.


def introduction():
    cprint("Welcome to my Mū tōrere game, made by Manav Gandhi!", cpu_colour)
    name_list.append(input("Player 1, please enter your name: "))
    # This asks for the name of the first player, appending it to a list.

    cprint(name_list[0] + " you are the Blue Perepere.", p1_colour)
    # Then greats them to the game

    time.sleep(delay_one)
    name_list.append(input("Player 2, please enter your name: "))
    #This asks for the name of the second player, appending it to a list.

    cprint(name_list[1] + " you are the Red Perepere.", p2_colour)
    time.sleep(delay_one)
    # Then greats them to the game.
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
        # If yes it will continue onward to the game.

    elif rules_check == "no":
        rules()
        # If no it will print the rules function.

    else:
        print("I'll take that as a yes...")
        time.sleep(delay_one)
        # If the player doesn't enter yes or no, it will print a msg and continue.

    return name_list
    # This returns the name_list variable to be used later in the code.

    # returns the name_list to the main code, useful in the while loop.


def move_logic(player_moves, turn):
    # This function is the main move logic of the game.

    while True:
        # This while loop is the main loop of the move_logic function.

        player_move = input(
            f"{name_list[turn - 1]} ({players[turn]}) What piece would you like to move? "
        )
        # This asks the player what piece they want to move.

        if exit_game(player_move):
            return True
            # Checks if input is in ext_list, if so it exits the game.

        try:
            player_move = int(player_move)
            # This trys making the player move and integer.

            if 1 <= player_move <= 9 and spots[player_move] == colored(
                    players[turn], color_mapping[players[turn]]):
                # This checks if the player move is a number between 1 and 9.
                # And if the player move is the same as the players colour.

                new_position = moved_piece(player_move, spots)
                # This calls the moved_piece function, assigning it to new_position.

                if new_position is not None:
                    spots[new_position] = colored(players[turn],
                                                  color_mapping[players[turn]])
                    # This checks if the new_position is not none.
                    # It will assign the spots[new_position] with the players colour.

                    spots[player_move] = "0"
                    # This assigns the spots[player_move] with 0.
                    player_moves.append(player_move)
                    # This appends the player_move to the player_moves list.

                    return False
                    # This returns false to the main code.
                else:
                    cprint(
                        f"Invalid move {name_list[turn - 1]}. Please try again.",
                        error_colour)
                    time.sleep(delay_one)
                    continue
                    # This prints an error message and asks the player to try again.

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
    # This function checks if the player's move is valid and if it is, it returns the value.

    connecting_spots = {
        1: [8, 2, 9],
        8: [7, 1, 9],
    }
    # This dictionary stores the spots that are on the top end of the main board.

    if player_move in connecting_spots:
        # This checks if plater_move is in the connecting_spots dictionary.

        available_spots = connecting_spots[player_move]
        # This is then assigned to the the available_spots.

        for spot in available_spots:
            # This for loop checks if the available_spots is in the spots dictionary.

            if player_move == 1:
                # This checks if the player_move is 1.

                if spots[8] == players[turn] and spots[2] == players[turn]:
                    # If it is it will check its connecting spots.

                    return None
                    # returning none if the player move is not valid.

                else:
                    if spots[spot] == '0':
                        return spot
                        # it will return spots if its value is '0'.

            elif player_move == 8:
                # This checks if the player_move is 8.

                if spots[7] == players[turn] and spots[1] == players[turn]:
                    # If it is it will check its connecting spots.

                    return None
                    # returning none if the player move is not valid.

                else:
                    if spots[spot] == '0':
                        return spot
                        # it will return spots if its value is '0'.

            else:
                # This else is if the player_move is not 1 or 8, boundray check.

                return None
                # returning none if the player move is not valid.

    elif player_move == 9:
        # This checks if the player_move is 9.

        for zero in spots:
            # This for loop checks if the spots is in the spots dictionary.

            if spots[zero] == '0':
                # This checks if the player's move is on the putahi.

                return zero
                # Returning zero if it is.

    else:
        # This else is if the player_move is not 1, 8 or 9, boundray check.

        if spots[player_move - 1] == colored(players[turn], color_mapping[
                players[turn]]) and spots[player_move + 1] == colored(
                    players[turn], color_mapping[players[turn]]):
            # Checks if spot is on either side of player_move.

            return None
            # If it is it will return none.

        if player_move - 1 in spots and spots[player_move - 1] == '0':
            return player_move - 1
            # This checks it the move - 1 is empty. If yes, value return.

        elif player_move + 1 in spots and spots[player_move + 1] == '0':
            return player_move + 1
            # This checks it the move + 1 is empty. If yes, value return.

        elif spots[9] == '0':
            return 9
            # This checks if the putahi is empty. If it is, it returns the 9.
        else:
            return None
            # else none.


def winning_logic(spots, players):
    # This function checks if either has player has won the game.

    global win
    # This makes the win variable global.

    current_player = players[turn]
    # makes players[turn] the current player

    current_player = colored(current_player, color_mapping[players[turn]])
    # makes the current player the colour of the player

    for key, value in spots.items():
        # This loop is used to find the empty spots(value) number(key).

        if value == '0':
            # This checks if the value is '0'.

            empty_spot = key
            # This assigns the empty_spot to the key.

            if empty_spot == 9:
                return False
            # This checks if the putahi is empty. If it is, it returns false.

            if empty_spot == 1:
                # This checks if the empty_spot is 1.

                if (spots.get(8) == current_player
                        and spots.get(2) == current_player
                        and spots.get(9) == current_player):
                    # This checks the spots around the empty_spot.

                    win = True
                    # If so win is True.

                else:
                    win = False
                # If not win is False.

            elif empty_spot == 8:
                # This elif is if the empty_spot is 8.

                if (spots.get(7) == current_player
                        and spots.get(1) == current_player
                        and spots.get(9) == current_player):
                    # This checks the spots around the empty_spot, 8 in this case.

                    win = True
                    # If so win is True.

                else:
                    win = False
                # If not win is False.

            else:
                # This else is if the empty_spot is not 1 or 8.

                if (spots.get(empty_spot + 1) == current_player
                        and spots.get(empty_spot - 1) == current_player
                        and spots.get(9) == current_player):
                    # This checks the spots around the empty_spot by using +1, -1, and 9.

                    win = True
                    # If so win is True.

    if win == False:
        return False
    # If win is false, it returns false.

    return win
    # Returns win to the whole program


# -----------------------------------------------------------------

# Everything below this line is the main game code.

# -----------------------------------------------------------------

name_list = introduction()
# This calls the introduction function and stores the player names in name_list.

while not win:
    # gameloop

    clear()
    # clears screen to remove excessive clutter.

    main_board()
    # prints main board(movable pieces).

    second_board()
    # prints second board(unmoveable pieces).

    if move_logic(player_moves, turn) is True:
        # This handles the bulk of the main program inputs validity checks and outputs.

        break
        # This breaks the loop if the game is exited.

    if winning_logic(spots, players) == True:

        clear()
        # clears screen to remove excessive clutter.
        
        main_board()
        # This prints the main board again to show final move.

        cprint("Congratulations " + name_list[turn - 1] + " wins!", cpu_colour)
        cprint("Thanks for playing Mu torere, made by Manav, see you later!",
               cpu_colour)
        # This checks if the winning_logic function is true, printing winner msg.

        win = True
        # This makes win true, ending the game loop.
        break
        # This breaks the game loop.

    turn += 1
    if turn > 2:
        turn = 1
    # Switch player turn
