from django.db import models
from django.contrib.auth.models import User 
from random import randint

class GameItem(models.Model):
	response = models.CharField(max_length = 64)
	opposite = models.CharField(max_length = 64)
	info = models.CharField(max_length = 64)
	coins = models.IntegerField("Cчет", default = 200)
	wins = models.IntegerField("Победы", default = 0)
	total_games = models.IntegerField("Всего игр", default = 0)
	win_rate_change = models.FloatField(default = randint(-5,5)+randint(-5,5)/10)
	is_selected = models.BooleanField(default = False)
	selected = models.CharField(max_length = 64)
	last_rate =  models.IntegerField("Последний приход", default = 0)
	my_wins = models.IntegerField("Мои обеды", default = 0)
	enemy_wins = models.IntegerField("Победы противника", default = 0)
	
	def __str__(self):
		return  f"{self.response} У противника {self.opposite}"

	def change_on(self, res, opp, inf, rate):
		self.total_games += 1
		self.last_rate = rate
		if inf == "win":
			self.wins += 1
			self.coins += rate
		elif inf == "lose":
			self.coins -= rate
		self.response = res
		self.opposite = opp
		self.info = inf
		return self

	owner = models.OneToOneField(
	User,
	on_delete=models.CASCADE,
	related_name='game'
	)