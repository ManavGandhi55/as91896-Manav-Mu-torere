def move_logic(player_moves, turn):
    while True:
        player_move = input(
            f"{name_list[turn - 1]} ({players[turn]}) What piece would you like to move?"
        )
        if exit_game(player_move):
            return True  # Exit the game
        try:
            player_move = int(player_move)
            if 1 <= player_move <= 9 and spots[player_move] == players[turn]:
                new_position = moved_piece(player_move, spots)
                if new_position is not None:
                    spots[new_position] = players[turn]
                    spots[player_move] = "0"
                    player_moves.append(
                        player_move)  # Add the move to player_moves
                    return False  # Valid move, continue the game

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
        except ValueError:
            cprint(f"Invalid move {name_list[turn - 1]}. Please try again.",
                   error_colour)
            time.sleep(delay_one)
            continue


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

