from rest_framework.viewsets import ModelViewSet
from applications.movies.serializers import MovieSerializer
from applications.movies.models import Movie
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from permissions.permissions import IsAuthor




class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['release_date']
    search_fields = ['title', 'genres', 'cast']

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        elif self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAuthenticated, IsAuthor]
        return super().get_permissions()
    

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()