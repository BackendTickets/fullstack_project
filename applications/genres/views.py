from rest_framework.viewsets import ModelViewSet
from applications.genres.serializers import GenreSerializer
from applications.genres.models import Genre
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    ilterset_fields = ['title']
    search_fields = ['title']
