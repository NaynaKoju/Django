from django.urls import path
from . import views

urlpatterns = [
    path("", views.start_game, name="start_game"), #goes on hangman automatic
    path("start/", views.start_game, name="start_game"),
    path("play/", views.play_game, name="play_game"),
]
