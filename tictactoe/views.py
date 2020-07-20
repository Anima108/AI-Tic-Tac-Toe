from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.http import JsonResponse
import random

class AjaxHandlerView(View):
	def get(self, request):
		if request.is_ajax():
			vector= request.GET.getlist('array[]')
			maxdepth= int(request.GET.get('difficulty_level'))
			player_marker= request.GET.get('player_marker')
			opponent_marker= request.GET.get('opponent_marker')
			isWild= int(request.GET.get('isWild'))
			optimization= int(request.GET.get('optimization'))

			if player_marker=='1':
			    player = 'x'
			    opponent= 'circle'
			else:
			    player= 'circle'
			    opponent= 'x'

			print(vector)
			print(player)
			print(opponent)
			print(maxdepth)
			print(optimization)


			def onetotwod(arr):
				board=[[0 for x in range(3)] for y in range(3)]
				k=0
				for i in range(3):
					for j in range(3):
						board[i][j]=arr[k]
						k=k+1
				return board

			ai= opponent
			human= player
			board=onetotwod(vector)
			##please check isWild from here
			##isWild #bool type

			scores={
				ai:-1 if isWild==1 else 1,
				human:+1 if isWild==1 else -1,
				"tie":0
			}

			def twotooned(row,col):
				index= col+3*row
				return index

			board= onetotwod(vector)


			def bestMove():
				#optimization correction
				if maxdepth==9:
					if(all(ele=='blank' for ele in vector)):
						if(isWild):
							return 4
						else:
							return (random.choice([0,2,6,8]))

				#Let's assume the bestScore is the minimum possible(so that we get a move)
				bestScore=-1000
				#creating a list of bestmove
				move=[]
				#AI to make its turn
				for i in range(3):
					for j in range(3):
						#Is the spot available?
						if board[i][j]=='blank':
							board[i][j]=ai #basically =player(us)
							score=minimax(board,0,False)
							board[i][j]='blank'
							if score>bestScore:
								bestScore=score
								move=[i,j]

				#board[move[0]][move[1]]=ai
				index=twotooned(move[0],move[1])
				return index


			def checkWinner():
				Winner = None
				for i in range(3):
					if board[i][0]== board[i][1]==board[i][2] and board[i][0]!='blank':
						Winner = board[i][0]
				for i in range(3):
					if board[0][i]== board[1][i]==board[2][i] and board[0][i]!='blank':
						Winner = board[0][i]

				if board[0][0]==board[1][1]==board[2][2] and board[0][0]!='blank':
					Winner = board[0][0]
				if board[2][0]==board[1][1]==board[0][2] and board[2][0]!='blank':
					Winner = board[2][0]

				openSpots = 0
				for i in range(3):
					for j in range(3):
						if board[i][j] == 'blank':
							openSpots= openSpots+1


				if Winner == None and openSpots == 0:
					return "tie"
				else:
					return Winner


			def minimax(board, depth, isMaximizing):
				if depth==maxdepth:
					return 0

				result =checkWinner()
				if result!=None:
					score=scores[result]
					return score

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

				else:
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

			aiMove= bestMove()
			return JsonResponse({'result': aiMove}, status=200)

		return render(request, "index.html")
