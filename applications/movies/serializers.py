from rest_framework import serializers
from applications.genres.serializers import GenreSerializer


from applications.movies.models import Movie
class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ['title']