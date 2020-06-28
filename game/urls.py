from django.urls import path
from . import views

urlpatterns = [ 
	path('play/', views.PlayView.as_view(), name  = 'play'),
	path('list/', views.GameListView.as_view() , name = 'list'),
	path('profile/<name>', views.profile, name = 'profile'),
	path('how-to-play',views.how_to_play, name='how-to-play'),
	path('calculate/', views.calculate, name = 'calculate'),
	path('find_opponent/', views.find_opp, name = 'find_opponent'),
]