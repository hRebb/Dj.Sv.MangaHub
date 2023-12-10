from rest_framework import serializers
from .models import Book, Genre, Classification

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = ['name']

class BookSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True, source='genre.all')
    classification = ClassificationSerializer(many=True, read_only=True, source='classification.all')

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'rating', 'read', 'genre', 'classification']

    def create(self, validated_data):
        genre_data = validated_data.pop('genre', [])
        classification_data = validated_data.pop('classification', [])

        book_instance = Book.objects.create(**validated_data)

        for genre_item in genre_data:
            genre_instance, created = Genre.objects.get_or_create(**genre_item)
            book_instance.genre.add(genre_instance)

        for classification_item in classification_data:
            classification_instance, created = Classification.objects.get_or_create(**classification_item)
            book_instance.classification.add(classification_instance)

        return book_instance
