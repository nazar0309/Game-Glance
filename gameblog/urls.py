from . import views
from django.urls import path
from .views import search_games

urlpatterns = [
    path('', views.GameList.as_view(), name='home'),
    path('search/', search_games, name='search_games'),
    path('<slug:slug>/', views.game_detail, name='game_detail'),
]