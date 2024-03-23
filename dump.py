while player1 or player2 not nameunvalid:
if not isinstance(player1, str) or not isinstance(player2,str): 
    raise nameunvalid
    if isinstance(player1, str) and isinstance(player2,str): 


def move(board_changer, moved_piece, current_player):
# if turn == 1 else turn == 2:
	players[1] = str(1 if turn == 1 else 2)
	move = int(input("Enter the number of the spot you want to move to: "))
	player_moves.append(move)
	moved_piece(player_moves, spots)
	board_changer(moved_piece, player_moves, spots, current_player)




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
			print("Invalid move. Please try again.")
			return None


def board_changer(moved_piece, player_moves, spots, current_player):
	if isinstance(moved_piece, int):
		spots.update({player_moves: players[current_player]})
	else:
		print("what the flip dude •`_´•")
