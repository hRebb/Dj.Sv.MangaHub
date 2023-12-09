from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Classification(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre)
    classification = models.ManyToManyField(Classification)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    read = models.BooleanField(default=False)