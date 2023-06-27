from rest_framework.viewsets import ModelViewSet
from applications.movies.serializers import MovieSerializer
from applications.movies.models import Movie

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer