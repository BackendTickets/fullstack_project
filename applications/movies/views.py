from rest_framework.viewsets import ModelViewSet
from movies.serializers import MovieSerializer
from .models import Movie

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer