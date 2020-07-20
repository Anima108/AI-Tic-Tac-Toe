def onetotwod(arr):
	board=[[0 for x in range(3)] for y in range(3)]
	k=0
	for i in range(3):
		for j in range(3):
			board[i][j]=arr[k]
			k=k+1
	return board

def twotooned(row,col):
	index= col+3*row
	return index
