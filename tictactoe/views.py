from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.http import JsonResponse
import random
from tictactoe.conversion import *
from tictactoe.minimax import *

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

			ai= opponent
			human= player
			board= onetotwod(vector,n)
			##please check isWild from here
			##isWild #bool type

			scores={
				ai:-1 if isWild==1 else 1,
				human:+1 if isWild==1 else -1,
				"tie":0
			}


			def bestMove():
				#optimization correction
				if maxdepth==n*n and optimization==1:
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
				for i in range(n):
					for j in range(n):
						#Is the spot available?
						if board[i][j]=='blank':
							board[i][j]=ai #basically =player(us)
							score=minimax(board,0,False,n)
							board[i][j]='blank'
							if score>bestScore:
								bestScore=score
								move=[i,j]

				#board[move[0]][move[1]]=ai
				index=twotooned(move[0],move[1],n)
				return index


			aiMove= bestMove()
			return JsonResponse({'result': aiMove}, status=200)

		return render(request, "index.html")
