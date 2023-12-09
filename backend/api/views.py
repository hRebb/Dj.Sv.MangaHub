from rest_framework import viewsets
from .serializers import BookSerializer, GenreSerializer
from .models import Book, Genre

# Create your views here.

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer