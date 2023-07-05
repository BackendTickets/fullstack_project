from django.db import models
from django.contrib.auth.models import User
from applications.movies.models import Movie



class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
