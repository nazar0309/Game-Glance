from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render
from gameblog.models import Game, Review

def profile_view(request):
    games = Game.objects.all()  # Fetch all games
    user_reviews = Review.objects.filter(author=request.user).order_by('-created_on')
    query = request.GET.get('q')  # Get the search query from the request
    
    # Initialize reviews to user's reviews if no query is made
    reviews = user_reviews  # By default, display all user reviews if no query is made
    info = 'You have not reviewed any games yet.'  # Default message if user has not reviewed any games
    # Check if there is a search query
    if query:
        # Try to find an exact match first
        query = query.strip()  # Remove any leading/trailing whitespace
        query = query.lower()  # Convert the query to lowercase
        reviews = user_reviews.filter(game__title__iexact=query)  # Filter by exact match on game title
        info = "No match found."
        if not reviews.exists():
            # If no exact match, continue to filter for substring matches
            reviews = user_reviews.filter(game__title__icontains=query)
    
    # Render the template with games and reviews
    return render(request, 'profile.html', {'games': games, 'reviews': reviews, 'info': info})
