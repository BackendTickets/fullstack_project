from django.db import models
from applications.genres.models import Genre

class Movie(models.Model):
    
    title = models.CharField(max_length=255)
    image = models.URLField()
    cast = models.CharField()
    link = models.URLField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    release_date = models.DateField()
    director = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.FloatField()
    duration = models.DurationField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'