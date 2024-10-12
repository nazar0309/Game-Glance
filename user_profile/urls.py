from django.urls import path
from .views import profile_view
from gameblog.views import delete_review, edit_review

urlpatterns = [
    path('review/delete/<int:review_id>/', delete_review, name='delete_review'),
    path('review/edit/<int:review_id>/', edit_review, name='edit_review'),
    path('', profile_view, name='profile_url'),
]
