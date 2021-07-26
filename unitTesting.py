import copy
from tictactoe import *

#def player(board):

#	if board == initial_state():
#		return X

	# using itteration method
	# As the board is 3X3 two dimentional array we need two itters to reach each position on the board to check which player has higher number of position on the board, we will keep track of numbers of position through X_times for X and O_times for O.
	# for i in range(len(board)):
	# 	for j in range(3):
	# 		if board[i][j] == X:
	# 			X_times += 1
	# 		elif board[i][j] == O:
#	# 			O_times += 1
#
#	X_times, O_times = 0, 0
#
#	# using count method on a list after looping over 1st dimention.
#	for row in board:
#		X_times += row.count(X)
#		O_times += row.count(O)
#
#	# the player who has lower numbers of position on board will go next
#	if X_times < O_times:
#		return X
#	else:
#		return O

#	print(player([[X, X, X],
#	            [X, X, O],
#	            [X, O, O]]))

#	print(player(initial_state()))


#def actions(board):
    #traverse through 2-Dimentional array and check whether the position is EMPTY or not if so return a sets of possible_moves on the board
#	possible_moves = set()
#	for i in range(len(board)):
#		for j in range(3):
#			if board[i][j] == EMPTY:
#				possible_moves.add((i,j))
#
#	return possible_moves
#
#	print(actions([[X, X, X],
#	            [X, EMPTY, O],
#	            [X, O, O]]))		# {(1, 1)}
#	print(actions(initial_state()))	# {(0, 1), (1, 2), (2, 1), (0, 0), (1, 1), (2, 0), (0, 2), (2, 2), (1, 0)}


#def result(board, action):
    # transition model return a newBoard (state) after board takes and action and return a newboard (newstate)

#	if action not in actions(board):
#		raise Exception("Invalid Position")
#
#	newBoard = copy.deepcopy(board)
#
#	if newBoard[action[0]][action[1]] == EMPTY:
#		newBoard[action[0]][action[1]] = player(board)
#
#	return newBoard
#   
#
#board = [[EMPTY, EMPTY, O],
#		 [X, O, X],
#		 [EMPTY, O, X]]
#action = 0,0
#print(result(board, action))


#def winner(board):
#	# Winner must have same positions across top, middle and bottom rows.
#	for i in range(len(board)):
#		if board[i][0] == board[i][1] == board[i][2]:
#			if board[i][0] == X:
#				return X
#			elif board[i][0] == O:
#				return O
#
#	# or same position across left middle and right.
#	for i in range(3):
#		if board[0][i] == board[1][i] == board[2][i]:
#			if board[0][i] == X:
#				return X
#			elif board[0][i] == O:
#				return O
#
#	# or must have postions across diagonals.
#	if board[0][0] == board[1][1] == board[2][2]:
#		if board[0][0] == X:
#			return X
#		elif board[0][0] == O:
#			return O
#	elif board[0][2] == board[1][1] == board[2][0]:
#		if board[0][2] == X:
#			return X
#		elif board[0][2] == O:
#			return O
#
#board = [[X, O, EMPTY],
#		[O, O, X],
#		[O, O, X]]
#
#print(winner(board))

#def terminal(board):
#	if winner(board) == X:
#		return True
#	elif winner(board) == O:
#		return True
#	else:
#		count = 0
#		for each_arr in board:
#			count += each_arr.count(X)
#			count += each_arr.count(O)
#		if count == 9:
#			return True
#		else:
#			return False
#
#board = [[O, EMPTY, X],
#		[X, O, O],
#		[O, X, O]]
#
#print(terminal(board))

# def utility(board):
#     win = winner(board)
#     if win == X:
#         return 1
#     elif win == O:
#         return -1
#     else:
#         return 0
# 
# board = [[O, X, O],
# 		[X, O, O],
# 		[X, O, X]]
# 
# print(utility(board))


#def minimax(board):
#	# Check whether the game is over
#	if terminal(board):
#		return utility(board)
#
#	best_act = None
#	pos_inf = math.inf
#	neg_inf = -math.inf
#	if player(board) == X:
#		for action in actions(board):
#			value = max(neg_inf, min_val(result(board, action)))
#			best_act = action
#
#	elif player(board) == O:
#		for action in actions(board):
#			value = min(pos_inf, max_val(result(board, action)))
#
#	return best_act
#
#def min_val(board):
#	if terminal(board):
#		return utility(board)
#
#	pos_inf = math.inf
#	for action in actions(board):
#		value = min(pos_inf, max_val(result(board, action)))
#	return value
#
#def max_val(board):
#	if terminal(board):
#		return utility(board)
#
#	neg_inf = math.inf
#	for action in actions(board):
#		value = max(neg_inf, max_val(result(board, action)))
#	return value
#
action = (1, 1)
board = [[X, EMPTY, O],
 		[EMPTY, EMPTY, O],
 		[X, EMPTY, EMPTY]]

##print(minimax(board))
#
#def min_value(board):
#    if terminal(board):
#        return utility(board)
#    v = math.inf
#    for action in actions(board):
#        value = max_value(result(board, action))
#        if value < v:
#            v = value
#    return v
#
#
#def max_value(board):
#    if terminal(board):
#        return utility(board)
#    v = -math.inf
#    for action in actions(board):
#        value = min_value(result(board, action))
#        if value > v:
#            v = value
#    return v
#
#def minimax(board):
#    """
#    Returns the optimal action for the current player on the board.
#    """
#    opt_act = None
#
#    if terminal(board):
#        return None
#    
#    if player(board) == X:
#        inf = -math.inf
#        for action in actions(board):
#            value = min_value(result(board, action))
#            if value > inf:
#                inf = value
#                opt_act = action
#
#    elif player(board) == O:
#        inf = math.inf
#        for action in actions(board):
#            value = max_value(result(board, action))
#            if value < inf:
#                inf = value
#                opt_act = action
#    return opt_act

