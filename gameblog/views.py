from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Game, Review
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ReviewForm
from django.core.paginator import Paginator
from user_profile.views import profile_view


def game_list(request):
    queryset = Game.objects.order_by('-created_on')
    query = request.GET.get('q')

    if query:
        try:
            query = query.strip().lower()
            game = Game.objects.get(title__iexact=query)
            return HttpResponseRedirect(
                reverse('game_detail', args=[game.slug]))
        except Game.DoesNotExist:
            queryset = queryset.filter(title__icontains=query)

    paginator = Paginator(queryset, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "gameblog/index.html",
        {
            "page_obj": page_obj,
            "query": query,
            "is_paginated": paginator.num_pages > 1
        }
    )


def game_detail(request, slug):
    queryset = Game.objects.order_by('-created_on')
    game = get_object_or_404(queryset, slug=slug)
    reviews = game.reviews.all().order_by('-created_on')[:3]
    related_games = Game.objects.filter(
        genre=game.genre).order_by('-created_on')[:5]

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.game = game
            review.save()
            messages.success(
                request, "Review has been submitted"
            )

    review_form = ReviewForm()
    return render(
        request,
        "gameblog/game_review.html",
        {
            "game": game,
            "reviews": reviews,
            "review_form": review_form,
            "related_games": related_games
        }
    )


def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    messages.success(request, "Your review has been deleted.")
    next_url = request.POST.get('next', 'profile_view')
    return redirect(next_url)


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
    related_games = Game.objects.filter(
        genre=game.genre).order_by('-created_on')[:5]

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.game = game
            review.save()
            messages.success(
                request, "Review submitted and awaiting approval"
            )

    review_form = ReviewForm()
    return render(
        request,
        "gameblog/game_reviews_all.html",
        {
            "game": game,
            "reviews": reviews,
            "related_games": related_games,
            "review_form": review_form
        }
    )
    
    
    
    


