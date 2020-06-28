from django.shortcuts import render, redirect 
from random import randint, choice
from game.models import GameItem
from django.views.generic import ListView
from django.http import HttpResponse
from django.views.generic.detail import DetailView 
from accounts.models import Profile
from django.contrib.auth.models import User
from django.views import View
from collections import defaultdict
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
import time

class Choice(): 
	def __init__(self, chosen):
		self.choice = chosen
		if chosen == "Бумага":
			self.win = "Камень"
			self.lose = "Ножницы"
		elif chosen == "Камень":
			self.win = "Ножницы"
			self.lose = "Бумага"
		else:
			self.win = "Бумага"
			self.lose = "Камень" 

def reverse(arr):
	for i in range(0, int((len(arr)/2))):
		arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
	return arr

class PlayView(View):

	def post(self, request, *args, **kwargs):
		time.sleep(5)
		try:
			u = self.request.user
			g = GameItem.objects.filter(owner = u).first()
			change = g.win_rate_change
			if g.is_selected:
				chosen = g.selected
				g.is_selected = False
			else:
				chosen = "Бумага"
		except:
			return HttpResponse("no", content_type = "text/html" )
		rate = int(request.POST.get("rate", False))
		res = Choice(chosen)
		if randint(0,1000) <= 400 + change * 10:
			g = g.change_on("Поздравляем! Вы победили!", res.win, "win", rate)
		elif randint(0,1000) <= 500 + change * 10:
			g = g.change_on("К сожалению, вы програли!", res.lose, "lose", rate)
		else:
			g = g.change_on("У вас ничья!", res.choice, "draw", rate)
		g.save()
		
		return HttpResponse(f"{g.response};{g.opposite}-2;{g.info}", content_type = "text/html" )


	def get(self, request, *args, **kwargs):
		u = self.request.user
		if u.is_anonymous:
			messages.error(request, "Необходимо войти или зарегистрироваться!") 
			return redirect("list")
		gm = GameItem.objects.filter(owner = u).first()
		return render(request, 'game/play.html', {"gm": gm})

class GameListView(ListView):
	
	def get(self, request, *args, **kwargs):
		
		def default():
			return 0

		d = defaultdict(default)
		for u in User.objects.all():
			wins = GameItem.objects.filter(owner = u).first().wins
			d[u] = wins

		d_list = list(d.items())
		d_list.sort(key = lambda i: i[1])
		res = reverse(d_list[-3:len(d_list)])
		players = randint(750, 1000)
		
		return render(request, "game/list.html", {"res": res, "players": players})

def profile(request, name):
	if request.method == "GET":
		u = User.objects.get(username = name)
		gi = GameItem.objects.filter(owner = u).first()
		wins = gi.wins
		total_games = gi.total_games
		if total_games != 0:
			percentage = wins * 100 / total_games
		else:
			percentage = 0
		return render(request,"game/profile.html",
			{	
				"last_rate": gi.last_rate,
				"last_game": gi.info,
				"cur_user": u,
	    		"wins": wins, 
	    		"total_games": total_games, 
	    		"percentage":round(percentage,2),
	    		"coins": gi.coins
	    	}
	    )

	return render(request,"game/list.html")

def how_to_play(request):
	return render(request,"game/how_to_play.html")

def calculate(request):
	if request.method == "POST":
		choice = request.POST.get("choice", False)
		u = request.user
		g = GameItem.objects.filter(owner = u).first()
		g.is_selected = True
		g.selected = choice
		g.save()

	return HttpResponse('ok', content_type = "text/html")

def get_all_id():
	users_id = []
	for u in User.objects.all():
		users_id.append(u.id)

	return users_id

def find_opp(request):
	if request.method == "POST":
		time_sleep = int(request.POST.get("time", False))
		users_id = get_all_id()
		opp = choice(users_id)
		while request.user.id == opp:
			opp = choice(users_id)

		opp = User.objects.get(id = opp)
		image_url = opp.profile.get_url()
		if image_url == None:
			image_url = "/media/anonym/profile.jpg"
		print(image_url)
		time.sleep((time_sleep-75)/1000)
		return HttpResponse(f"{opp.username};{image_url}",content_type = "text/html")

	return redirect("list")


