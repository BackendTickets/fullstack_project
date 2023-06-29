from rest_framework import routers

from applications.movies.views import MovieViewSet

router = routers.DefaultRouter()
router.register('applications/movies', MovieViewSet, basename='applications.movies')
urlpatterns = router.urls