from django.contrib import admin

# Register your models here.
# /movie/admin.py

from .models import Movie
admin.site.register(Movie)