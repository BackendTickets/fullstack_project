from rest_framework.viewsets import ModelViewSet
from applications.movies.serializers import MovieSerializer
from applications.movies.models import Movie
from permissions.permissions import IsOwnerOrIsAdminUser
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsOwnerOrIsAdminUser]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super().get_permissions()
