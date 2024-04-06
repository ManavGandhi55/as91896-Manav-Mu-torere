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