from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Review, Comment, Like
from .serializers import ReviewSerializer, CommentSerializer, LikeSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        review = self.get_object()
        user = request.user
        like, created = Like.objects.get_or_create(user=user, review=review)
        if not created:
            like.delete()
        return Response({'detail': 'Like updated successfully.'})

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer