from rest_framework.viewsets import ModelViewSet
from applications.genres.serializers import GenreSerializer
from applications.genres.models import Genre

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    search_fields = ['title']
