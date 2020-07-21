def onetotwod(arr,n):
	board=[[0 for x in range(n)] for y in range(n)]
	k=0
	for i in range(n):
		for j in range(n):
			board[i][j]=arr[k]
			k=k+1
	return board

def twotooned(row,col,n):
	index= col+n*row
	return index
