from django.contrib import admin
from .models import Book, Genre, Classification

# Register your models here.
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Classification)
