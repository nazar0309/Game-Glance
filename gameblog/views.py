from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Game
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ReviewForm


class GameList(generic.ListView):
    queryset = Game.objects.order_by('-created_on')
    template_name = "gameblog/index.html"
    paginate_by = 8
    
def game_detail(request, slug):
    queryset = Game.objects.order_by('-created_on')
    game = get_object_or_404(queryset, slug=slug)
    reviews = game.reviews.all().order_by('-created_on')[:3]
    related_games = Game.objects.filter(genre=game.genre).order_by('-created_on')[:5]
    
    if request.method == "POST":
        print('Getting the POST request...')
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.game = game
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review submitted and awaiting approval'
                )

    review_form = ReviewForm()
    print('Rendering template...')
    
    return render(
        request,
        "gameblog/game_review.html",
         {"game": game,
         "reviews": reviews,
         "review_form": review_form,
         'related_games': related_games
        },
    )
    
    


