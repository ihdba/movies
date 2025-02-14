from django.db import models

from django.contrib import admin



class Movie(models.Model):
    
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/')
    
    def __str__(self):
        return str(self.id) + ' ' + self.name
    

