from rest_framework import serializers
from.models import Book, Genre, Classification

class GenreSerializer(serializers.Serializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ClassificationSerializer(serializers.Serializer):
    class Meta:
        model = Classification
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'