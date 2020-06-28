from django.contrib import admin
from game.models import GameItem

@admin.register(GameItem)
class GameItemAdmin(admin.ModelAdmin):
	list_display = ('response', 'opposite', 'info')
