from django.db import models

class Movie(models.Model):
    GENRE_CHOICES = (
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('fantasy', 'Fantasy'),
        ('horror', 'Horror'),
        ('sci-fi', 'Science Fiction'),
    )

    title = models.CharField(max_length=255)
    image = models.URLField()
    cast = models.CharField()
    link = models.URLField()
    release_date = models.DateField()
    director = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genres = models.CharField(max_length=20, choices=GENRE_CHOICES)
    duration = models.DurationField()

    def __str__(self):
        return self.title
