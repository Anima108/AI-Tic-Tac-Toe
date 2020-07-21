def checkWinner(board,n):
	Winner = None
	for i in range(n):
		if board[i][0]== board[i][1]==board[i][2] and board[i][0]!='blank':
			Winner = board[i][0]
	for i in range(n):
		if board[0][i]== board[1][i]==board[2][i] and board[0][i]!='blank':
			Winner = board[0][i]

	if board[0][0]==board[1][1]==board[2][2] and board[0][0]!='blank':
		Winner = board[0][0]

	if board[2][0]==board[1][1]==board[0][2] and board[2][0]!='blank':
		Winner = board[2][0]

	openSpots = 0

	for i in range(n):
		for j in range(n):
			if board[i][j] == 'blank':
				openSpots= openSpots+1


	if Winner == None and openSpots == 0:
		return "tie"

	else:
		return Winner
