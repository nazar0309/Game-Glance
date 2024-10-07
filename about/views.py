# user_profile/views.py

from django.shortcuts import render
from .models import About

def about_view(request):
    return render(request, 'profile.html')
