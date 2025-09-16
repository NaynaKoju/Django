from django.urls import path
from . import views

urlpatterns = [
    path("", views.start_game, name="start_game"), #goes on hangman automatic
    path("start/", views.start_game, name="start_game"),
    path("play/", views.play_game, name="play_game"),
    path("quit/", views.quit_game, name="quit_game"),
    path('reset_wins/', views.reset_wins, name='reset_wins'),

]
