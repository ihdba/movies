from django.db import models

from django.contrib import admin
from django.contrib.auth.models import User



class Movie(models.Model):
    
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/')
    
    def __str__(self):
        return str(self.id) + ' ' + self.name
    


class Review(models.Model):
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return str(self.movie)