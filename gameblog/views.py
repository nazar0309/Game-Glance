from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Game
from django.http import HttpResponseRedirect
from django.contrib import messages


class GameList(generic.ListView):
    queryset = Game.objects.order_by('-created_on')
    template_name = "gameblog/index.html"
    paginate_by = 4
    
def game_detail(request, slug):
    queryset = Game.objects.order_by('-created_on')
    game = get_object_or_404(queryset, slug=slug)
    
    return render(
        request,
        "gameblog/game_review.html",
        {'game': game}
    )

