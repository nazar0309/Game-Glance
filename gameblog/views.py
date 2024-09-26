from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Game
from django.http import HttpResponseRedirect
from django.contrib import messages


class GameList(generic.ListView):
    queryset = Game.objects.filter(status=1)
    template_name = "gameblog/index.html"
    paginate_by = 3
