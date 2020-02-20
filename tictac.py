import random 

my_board = [' '] * 10


def game_board(board):
		# how game board will display
		print('|'+board[7]+' | '+board[8]+' | '+board[9]+'|')
		print('-----------')
		print('|'+board[4]+' | '+board[5]+' | '+board[6]+'|')
		print('-----------')
		print('|'+board[1]+' | '+board[2]+' | '+board[3]+'|')

# game_board(my_board)

def player_input():
	# asking input until valid input is entered  
	marker = ''
	while marker != 'X' and marker != 'O':
		marker = input('Choose X or O: ').upper()
		if marker == 'X' or marker == 'O':
			pass
		else:
			print('Invalid input!')

	player1 = marker
		
	if player1 == 'X':
		player2 =  'O'
	else:
		player2 = 'X'
	return (player1, player2)
			

 #player1, player2 = player_input()

 #print(player1, player2)



def assign_marker(board, position, marker):
	board[position] = marker

# assign_marker(my_board, 2, player1)
# game_board(my_board)


def check_result(board, marker):
	return ((board[7] == board[8] == board[9] == marker) or \
			(board[4] == board[5] == board[6] == marker) or \
			(board[1] == board[2] == board[3] == marker) or \
			(board[7] == board[4] == board[1] == marker) or \
			(board[8] == board[5] == board[2] == marker) or \
			(board[9] == board[6] == board[3] == marker) or \
			(board[1] == board[5] == board[9] == marker) or \
			(board[3] == board[5] == board[7] == marker))

def first_pick():
	x = random.choice(['Player1', 'Player2'])
	return x



def space_check(board, position):
	return board[position] == ' '



def full_check(board):
	for i in range(1, 10):
		if space_check(board, i):
			return False
	return True


def choose_pos(board):
	pos = 0
	while pos not in [1,2,3,4,5,6,7,8,9] and not space_check(board, pos):
		pos = int(input('Enter position: '))
	return pos

def play_again():
	return input('Do you want to play again? Yes/No: ').upper().startswith('Y')



while True:
	
	print('\n'*100)
	play = input('Play the game? Yes/No: ').upper()
	if play[0] == 'Y':
		game_on = True
	else:
		game_on = False
		break
	player1, player2 = player_input()

	if player1 == 'X':
		print('Player1 marker is X')
		print('Player2 marker is O')
	else: 
		print('Player1 marker is O')
		print('Player2 marker is X')

	turn = first_pick()
	print(turn + ' will go first. ')

	
	while game_on:

		if turn == 'player1':
			game_board(my_board)
			position = choose_pos(my_board)
			assign_marker(my_board, position, player1)

			if check_result(my_board, player1):
				game_board(my_board)
				print('Congrats, Player1 wins the match...')
				game_on = False

			else:
				if full_check(my_board):
					game_board(my_board)
					print('The game is tie...')
					break
				else:	
					turn = 'Player2'

		else:
			game_board(my_board)
			position = choose_pos(my_board)
			assign_marker(my_board, position, player2)

			if check_result(my_board, player2):
				game_board(my_board)
				print('Congrats Player2 wins the match...')
				game_on = False

			else:
				if full_check(my_board):
					game_board(my_board)
					print('The game is tie...')
					break
				else:
					turn = 'player1'

	if not play_again():
		break
	

