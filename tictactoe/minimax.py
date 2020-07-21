from tictactoe.winner import *

def minimax(board, depth, isMaximizing,n):
	if depth==maxdepth:
		return 0

	result =checkWinner(board,n)
	if result!=None:
		score=scores[result]
		return score

	if(isMaximizing):
		bestScore = -1000
			for i in range(n):
				for j in range(n):
					#Is the spot available?
					if board[i][j]=='blank':
						board[i][j] = ai
						score = minimax(board,depth+1,False,n)
						board[i][j]='blank'
						bestScore = max(score, bestScore)

		return bestScore

	else:
		bestScore = 1000
			for i in range(n):
				for j in range(n):
					#Is the spot available?
					if board[i][j]=='blank':
						board[i][j] = human
						score = minimax(board,depth+1,True,n)
						board[i][j]='blank'
						bestScore = min(score, bestScore)

		return bestScore
