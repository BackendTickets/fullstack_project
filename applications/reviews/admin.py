from django.contrib import admin
from .models import Review, Comment, Like

admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Like)