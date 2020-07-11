# Microsoft-Codess Tic-Tac-Toe! ⭕️ ❌ ⭕️  
#### A 'Mars Colonization :volcano:' theme web application which makes use of the minimax algorithm to create an unbeatable version of the famous Noughts and Crosses game!  

![alt text](https://github.com/Anima108/My-Codes/blob/master/src/Mars%20Colonization.jpg "Mars Colonization")  

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Languages Used:
**Algorithm**- Python  
**Library used**- random  
**Frontend**- HTML, CSS, JavaScript    

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```python
def minimax(board, depth, isMaximizing):
# Check the depth condition
if depth==maxdepth:
	return 0
```  
```python
# Check the winning condition at every situation
result =checkWinner()
if result!=None:
	score=scores[result]
	return score
```  
```python
#Turn of Maximizing player(this player will always try to maximize the score)
# we will check the score of every move and will return the maximum one.
if(isMaximizing):
bestScore = -1000
	for i in range(3):
		for j in range(3):
			#Is the spot available?
			if board[i][j]=='blank':
				board[i][j] = ai
				score = minimax(board,depth+1,False)
				board[i][j]='blank'
				bestScore = max(score, bestScore)

return bestScore
```  
```python
#Turn of Minimizing player(this player will always try to minimize the score)
# we will check the score of every move and will return the minimum one.
if(!isMaximizing):
	bestScore = 1000
	for i in range(3):
		for j in range(3):
			#Is the spot available?
			if board[i][j]=='blank':
			board[i][j] = human
			score = minimax(board,depth+1,True)
			board[i][j]='blank'
			bestScore = min(score, bestScore)

return bestScore
```



      
