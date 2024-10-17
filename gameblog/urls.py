from . import views
from django.urls import path

urlpatterns = [
    path('', views.GameList, name='home'),
    path('<slug:slug>/', views.game_detail, name='game_detail'),
    path('<slug:slug>/reviews/', views.game_reviews_all, name='game_reviews_all'),
]