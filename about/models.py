from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    def __str__(self):
        return self.title