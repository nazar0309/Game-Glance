# user_profile/views.py
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render
from gameblog.models import Game, Review

def profile_view(request):
    games = Game.objects.all()  # Fetch all games
    # Assuming that Review is the model where reviews are stored and it has a ForeignKey to Game and User
    user_reviews = Review.objects.filter(author=request.user)  # Fetch reviews by the logged-in user

    return render(request, 'profile.html', {'games': games, 'reviews': user_reviews})


def delete_review(request, review_id):
    if request.method == "POST":
        review = get_object_or_404(Review, id=review_id)
        review.delete()
        return JsonResponse({"success": True})

# Edit Review View (Example for AJAX or form submission)
def edit_review(request, review_id):
    if request.method == "POST":
        review = get_object_or_404(Review, id=review_id)
        new_body = request.POST.get('body', '')
        if new_body:
            review.body = new_body
            review.save()
            return JsonResponse({"success": True, "new_body": new_body})
    return JsonResponse({"success": False})