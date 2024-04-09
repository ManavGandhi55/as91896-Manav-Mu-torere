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
    if spots[0] == 0:
        if connecting_spots[1] are all the same players piece 
        win = True
        if connecting_spots[8] are all the same players piece 
        win = True
        if spots[zero - 1] == colored(players[turn], color_mapping[
            players[turn]]) and spots[zero + 1] == colored(
                players[turn], color_mapping[players[turn]]):
        win = True
        if spots[ze
        return win




# winngin logic down below
# 1
# 1 

empty_spot = find_empty_spot(spots)
if empty_spot == 1:
    if connecting_spots[1] == colored(players[turn - 1], color_mapping[players[turn - 1]]):
        win = True
        print("true")
        return win
elif empty_spot == 8:
    if connecting_spots[8] == colored(players[turn - 1], color_mapping[players[turn - 1]]):
        win = True
        print("true")
        return win
elif (spots[empty_spot - 1] == colored(players[turn - 1], color_mapping[players[turn]]) and
spots[empty_spot + 1] == colored(players[turn - 1], color_mapping[players[turn]]) and colored(players[turn - 1])) == 9:
    win = True
    print("true")
    return win


# wining logic down below
# 2
# 2
def winning_logic(spots):
    for key, value in spots:
        if value == '0':
            empty_spot = key
            if empty_spot == 1:
                if (spots[8] == players[turn] and spots[2] == players[turn]):
                    win = True
                    print("true")
            elif empty_spot == 8:
                if (spots[7] == players[turn] and spots[1] == players[turn]):
                    win = True
                    print("true")
            elif spots[empty_spot - 1] == colored(
                    players[turn],
                    color_mapping[players[turn]]) and spots[empty_spot + 1] == colored(
                        players[turn], color_mapping[players[turn]]):
                win = True
                print("true")

            if win == True:
                cprint("Congraulations " + name_list[turn] + " WINS!!!", cpu_colour)
                time.sleep(delay_one)
                os.system('cls' if os.name == 'nt' else 'clear')
                break


# winning logic 3 
# 3 
# 3
def winning_logic(spots):
global win
for key, value in spots.items():
    if value == '0':
        empty_spot = key
        if empty_spot == 1:
            if (spots[8] == players[turn - 1] and spots[2] == players[turn - 1] and spots[9] == players[turn - 1]):
                win = True
            else:
                win = False
        elif empty_spot == 8:
            if (spots[7] == players[turn - 1] and spots[1] == players[turn - 1] and spots[9] == players[turn - 1]):
                win = True
            else:
                win = False
        elif empty_spot + 1 in spots and spots[empty_spot - 1] and spots[9] == colored(players[turn - 1], color_mapping[players[turn - 1]]):
            win = True
        else:
            win = False

return win   


# BOARDS 
# 1
# 1

def main_board():
    print('\n     ' + spots[8] + '  -  ' + spots[1] + '   ')
    print('    \\       /')
    print('   ' + spots[7] + '         ' + spots[2] + '')
    print('   -    ' + spots[9] + '    -')
    print('   ' + spots[6] + '         ' + spots[3] + '   ')
    print('    /       \\')
    print('     ' + spots[5] + '  -  ' + spots[4] + '   ')


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