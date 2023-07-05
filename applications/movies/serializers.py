from rest_framework import serializers
from applications.genres.serializers import GenreSerializer
from applications.movies.models import Movie
from applications.genres.models import Genre

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, required=False)

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        genres_data = validated_data.pop('genres', [])
        movie = Movie.objects.create(**validated_data)

        for genre_data in genres_data:
            # Создание или получение объекта жанра из приложения genres
            genre, _ = Genre.objects.get_or_create(**genre_data)
            movie.genres.add(genre)
        
        movie.save()

        return movie