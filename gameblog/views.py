from django.shortcuts import render, get_object_or_404, reverse
from .models import Game
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ReviewForm
from django.core.paginator import Paginator


        
def GameList(request):
    queryset = Game.objects.order_by('-created_on')  # Get all games ordered by created_on
    query = request.GET.get('q')  # Get the search query from the request
    
    # Check if there is a search query
    if query:
        # Try to find an exact match first
        try:
            game = Game.objects.get(title__iexact=query)  # Try to get the exact match
            return HttpResponseRedirect(reverse('game_detail', args=[game.slug]))  # Redirect to game detail if found
        except Game.DoesNotExist:
            # If no exact match, continue to filter for substring matches
            queryset = queryset.filter(title__icontains=query)  # Filter games by the search query

    # Set up pagination
    paginator = Paginator(queryset, 8)  # Show 8 games per page
    page_number = request.GET.get('page')  # Get the page number from the URL query parameters
    page_obj = paginator.get_page(page_number)  # Get the specific page of results

    # Render the template with the paginated results and query
    return render(request, "gameblog/index.html", {
        "page_obj": page_obj, 
        "query": query, 
        "is_paginated": paginator.num_pages > 1
    }) 
    
    
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
    
    
    
    


