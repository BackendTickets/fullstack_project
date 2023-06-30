from rest_framework import routers
from applications.genres.views import GenreViewSet


router = routers.DefaultRouter()
router.register('applications/genres', GenreViewSet, basename='applications.genres')
urlpatterns = router.urls
