from django.db import models

class Movie(models.Model):
    
    title = models.CharField(max_length=255)
    image = models.URLField()
    cast = models.CharField()
    link = models.URLField()
    release_date = models.DateField()
    director = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.DurationField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'