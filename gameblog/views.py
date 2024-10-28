from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Game, Review
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ReviewForm
from django.core.paginator import Paginator
from user_profile.views import profile_view


        
def GameList(request):
    queryset = Game.objects.order_by('-created_on')  # Get all games ordered by created_on
    query = request.GET.get('q')  # Get the search query from the request
    
    # Check if there is a search query
    if query:
        # Try to find an exact match first
        try:
            query = query.strip()  # Remove any leading/trailing whitespace
            query = query.lower()  # Convert the query to lowercase
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
                'Review has been submitted'
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
    
# View to delete a review
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    messages.success(request, "Your review has been deleted.")

    # Get the next URL from the form (which page the request originated from)
    next_url = request.POST.get('next', 'profile_view')  # Default to 'profile_view' if 'next' is not provided

    return redirect(next_url)

# View to edit a review
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Your review has been updated.")
            return redirect('profile_url')  # Redirect back to the profile page
    else:
        form = ReviewForm(instance=review)  # Pass the review instance to prepopulate the form

    # Pass the review object and the form to the template
    return render(request, 'edit_review.html', {'form': form, 'review': review})

def game_reviews_all(request, slug):
    queryset = Game.objects.order_by('-created_on')
    game = get_object_or_404(queryset, slug=slug)
    reviews = game.reviews.all().order_by('-created_on')
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
        "gameblog/game_reviews_all.html",
         {"game": game,
         "reviews": reviews,
         'related_games': related_games,
         "review_form": review_form
        },
    )
    
    
    
    


