'''Mū tōrere is a Moari board game played on an octagon shaped board, which has 9 spots 
to place the stones on, one on each corner of the octagon called periperi and lines 
connecting it to the center which is called the Putahi, which is the 9th spot. In order 
to win you have to try and block the opposing player from being able to make a name'''

import os

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


def introduction():
    print("Welcome to my Mū tōrere game, made by Manav Gandhi")
    player1 = input("Player 1, please enter your name: ")
    player2 = input("Player 2, please enter your name: ")
    name_list.append(player1)
    name_list.append(player2)
    # This is a part of code which asks the players for their playernames
    # Modifies name_list to include the names of the players.
    print("Welcome", name_list[0], "and", name_list[1],
          "to the traditional Maori game, Mū tōrere!")
    # This introduces the game to the players, including their playername variables
    rules_check = input("Do you know the rules of Mu torere: ").lower()
    if rules_check == "yes":
        print("Okay let's get started then...")
    else:
        print("The rules to Mu torere are very simple...")
        print(
            "The game is played on an 8-sided board, with 9 spots to place the Perepers's on as the spot in the middle (the putahi) is the 9th spot. Each player takes turns moving to an unoccupied spot on the board. Two players cannot occupy the same spot at the same time. In order to win, you need to block the opposing player from being able to move."
        )
        # This is the rules of the game, which it asks the player if they already know them or not.
        rules_finish = input("Are you finished reading the rules?: ").lower()
        if rules_finish == "yes":
            print("Okay let's get started then...")
        else:
            print("Well you'll figure it out along the way...")
        # Asks if they're finished reading the rules to Mu torere.
    print("The game will now begin...")
    return name_list


def move_logic():
    global player_moves
    player_move = int(
        input((name_list[turn - 1], "(", players[turn],
               ") What piece would you like to move?")))
    player_moves.append(player_move)
    new_position = moved_piece(player_move, spots)
    if new_position is not None:
        spots[new_position] = players[turn]
        spots[player_move] = "0"
    else:
        print("Invalid move. Please try again.")


def moved_piece(player_move, spots):
    connecting_spots = {
        1: [8, 2, 9],
        8: [7, 1, 9],
    }

    if player_move in connecting_spots:
        available_spots = connecting_spots[player_move]
        for spot in available_spots:
            if spots[spot] == '0':
                return spot
    elif player_move == 9:
        for zero in spots:
            if spots[zero] == '0':
                return zero
    else:
        if player_move - 1 in spots and spots[player_move - 1] == '0':
            return player_move - 1
        elif player_move + 1 in spots and spots[player_move + 1] == '0':
            return player_move + 1
        elif spots[9] == '0':
            return 9
        else:
            return None


# Start of game
name_list = introduction()

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
