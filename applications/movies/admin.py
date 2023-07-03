from django.contrib import admin
from applications.movies.models import Movie
from applications.reviews.models import Comment

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1  

class MovieAdmin(admin.ModelAdmin):
    inlines=[CommentInline]
    readonly_fields=['image']

admin.site.register(Movie)
