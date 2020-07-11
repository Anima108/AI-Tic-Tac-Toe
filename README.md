# Microsoft-Codess Tic-Tac-Toe! ⭕️ ❌ ⭕️  
#### A 'Mars Colonization :volcano:' theme web application which makes use of the minimax algorithm to create an unbeatable version of the famous Noughts and Crosses game!  

![alt text](https://github.com/Anima108/My-Codes/blob/master/src/Mars%20Colonization.jpg "Mars Colonization")  

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### Have a Personalised Experience at Mars!  
- [x] **Alien**:alien:  : Opponent    
- [x] **Human**:woman:  : Player  
- [x] **Marker**        : Select your own marker ⭕️/❌  
- [x] **First Move**    : Don't wish to play the first move? No worries!  
- [x] **Score Tracker** : Keep a track of all the games played yet  
- [x] **Level**         : Are you a beginner? Or an expert? You'll not be disappointed  
- [x] **Surprise Element**: Go wild :neckbeard:  

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Languages Used:
**Algorithm**- Python  
**Library used**- random  
**Frontend**- HTML, CSS, JavaScript    

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Addition of Depth  
Our Algorithm, makes use of 'maxdepth' to limit the difficulty level of the game against alien.  
At each recursive call from one given state 'depth' is incremented by one;
The variable maxdepth is responsible to keep check, whether the requested difficulty level has been reached or not and further limits the call to the MiniMax Algo.

```python
def minimax(board, depth, isMaximizing):
# Check the depth condition
if depth==maxdepth:
#Do not call the further function and directly return from here
	return 0
```

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### Do we have a winner yet?
```python
# Check the winning condition at every situation
result =checkWinner()
if result!=None:
	score=scores[result]
	return score
``` 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```python
# Turn of Maximizing player(this player will always try to maximize the score)
# We will check the score of every move and will return the maximum one.
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
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```python
# Turn of Minimizing player(this player will always try to minimize the score)
# We will check the score of every move and will return the minimum one.
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
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Optimization Technique:  
  
- With the variation of letting the **AI agent play the first chance**, the algorithm was taking an **unusually high time to decide its move**. 
	- This is due to the agent building all the possible cases and going till the terminal depth of the board. To eradicate this lag we made use of the game theory of tic-tac-toe.  

- Most experienced tic-tac-toe players put the **first marker in a corner** when they get to play first. This gives the opponent the most opportunities to make a mistake.      
	- Given the chance to play the first move, we asked our AI agent to pick a **random corner** from a list of all corners on the board.  

#### This technique, however small, reduced the initial time of picking a move from **9.016 seconds to 0.0001 seconds!**  

- Similarly, in Wild Tic-Tac-Toe the best move to be played, to give the opponent the most opportunities to make a mistake was the **centre block**.   

#### Reducing the time from **9.019 seconds to 0.0001 seconds!**  

```python
				if(all(ele=='blank' for ele in arr)):
					if(iswild==1):
						return 4
					else:
						return (random.choice([0,2,6,8]))
						``` 
