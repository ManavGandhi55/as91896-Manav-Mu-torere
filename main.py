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

exit_list = ["quit", "break", "lobby", "exit", "leave", "end", "stop", "end game"]
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

def exit(player_move):    
    if player_move in [item.lower() for item in exit_list]:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Thank you for playing Mū Tōrere!")
        time.sleep(delay_one)
        os.system('cls' if os.name == 'nt' else 'clear')
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
    player_move = input(f"{name_list[turn - 1]} ({players[turn]}) What piece would you like to move?")
    #This asks the player what piece they would like to move.
    valid_move = False
    exit(player_move)
    while valid_move is False:
        if str(player_move) not in [item.lower() for item in exit_list]:
            print(f"Invalid move {name_list[turn - 1]}. Please try again.")
            time.sleep(delay_one)
            player_move = int(
            input(
                f"{name_list[turn - 1]} ({players[turn]}) What piece would you like to move?"
            ))
    #This while loop checks if the player's move is valid.
        else:
            if 1 <= int(player_move) <= 9:
                if spots[int(player_move)] == players[turn]:
                #This checks if the player's move is valid.
                    
                    player_moves.append(player_move)
                    #This adds the player's move to the player_moves list.
                    
                    new_position = moved_piece(player_move, spots)
                    #This calls the moved_piece function to move the piece.
                    
                    if new_position is not None:
                        spots[new_position] = players[turn]
                        spots[player_move] = "0"
                        valid_move = True
                    #This checks if the player's move is valid and stops the while loop.
                    else:
                        print(f"Invalid move {name_list[turn - 1]}. Please try again.")
                        time.sleep(delay_one)
                        player_move = int(
                        input(
                            f"{name_list[turn - 1]} ({players[turn]}) What piece would you like to move?"
                        ))
                        
                    #This checks if the move is valid and if it is, it moves the piece, else error msg
                else:
                    print(f"Invalid move {name_list[turn - 1]}. Please try again.")
                    time.sleep(delay_one)
                    player_move = int(
                    input(
                        f"{name_list[turn - 1]} ({players[turn]}) What piece would you like to move?"
                    ))
                    
                    #This is just in case the code bugs out or smthn, it will go to the else function
            else:
                print(f"Invalid move {name_list[turn - 1]}. Please try again.")
                time.sleep(delay_one)
                player_move = int(
                input(
                    f"{name_list[turn - 1]} ({players[turn]}) What piece would you like to move?"
                ))
            


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
        if spots[player_move - 1] == players[turn] and spots[player_move + 1] == players[turn]:
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
    move_logic(player_moves, turn)
    # Handle player move
    

    turn += 1
    if turn > 2:
        turn = 1
    # Switch player turn
