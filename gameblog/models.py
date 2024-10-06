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
    youtube_url = models.URLField(max_length=500, blank=True, null=True)  # To store the YouTube URL

    def __str__(self):
        return self.title
    
class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer')
    body = models.TextField(max_length=200)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"Review {self.body} by {self.author}"
    
    
