from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from gameblog.models import Game, Review
from django.contrib.auth.decorators import login_required


@login_required
def profile_view(request):
    games = Game.objects.all()  # Fetch all games
    user_reviews = (
        Review.objects
        .filter(author=request.user)
        .order_by('-created_on')
    )
    query = request.GET.get('q')  # Get the search query from the request
    reviews = user_reviews  # Default: display all user reviews if no query
    info = 'You have not reviewed any games yet.'  # Default message

    # Check if there is a search query
    if query:
        query = query.strip().lower()  # Normalize the query
        reviews = user_reviews.filter(game__title__iexact=query)  # Exact match
        info = "No match found."

        if not reviews.exists():
            # Filter by substring match if no exact match found
            reviews = user_reviews.filter(game__title__icontains=query)

    # Render the template with games and reviews
    return render(
        request,
        'profile.html',
        {
            'games': games,
            'reviews': reviews,
            'info': info,
        }
    )
