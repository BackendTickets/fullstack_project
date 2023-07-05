from rest_framework import serializers
from applications.genres.serializers import GenreSerializer
from applications.movies.models import Movie
from applications.genres.models import Genre

class MovieSerializer(serializers.ModelSerializer):
    # genres = GenreSerializer(many=True, required=False)

    class Meta:
        model = Movie
        fields = '__all__'

    # def create(self, validated_data):
    #     genre_data = validated_data.pop('genre', None)

    #     movie = Movie.objects.create(**validated_data)

    #     if genre_data:
    #         genre, _ = Genre.objects.get_or_create(**genre_data)
    #         movie.genre = genre

    #     return movie