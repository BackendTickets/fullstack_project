from django.db import models
from applications.movies.models import Movie


class Genre(models.Model):
    GENRE_CHOICES = (
        ('action', 'Action'),
        ('adventure', 'Adventure'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('fantasy', 'Fantasy'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('sci-fi', 'Sci-Fi'),
    )

    title = models.CharField(max_length=100, choices=GENRE_CHOICES)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'