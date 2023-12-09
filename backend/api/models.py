from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.ManyToManyField(Genre)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    read = models.BooleanField(default=False)