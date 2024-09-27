from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=200)
    image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(max_length=2000, unique=True)
    description = models.TextField()
    release_date = models.DateField()
    company = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    platform = models.CharField(max_length=50)  # e.g., PC, PlayStation, Xbox
    created_on = models.DateTimeField(auto_now_add=True)  # Auto timestamp for when the game is added
    updated_on = models.DateTimeField(auto_now=True)      # Auto timestamp for last modification

    def __str__(self):
        return self.title
    
    