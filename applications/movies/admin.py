from django.contrib import admin
from applications.movies.models import Movie

class MovieAdmin(admin.ModelAdmin):
    readonly_fields=['image']

admin.site.register(Movie)
