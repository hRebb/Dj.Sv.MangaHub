from rest_framework import serializers
from.models import Book, Genre

class GenreSerializer(serializers.Serializer):
    class Meta:
        model = Genre
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'