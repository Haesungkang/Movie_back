from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.TextField()

class Movie(models.Model):
    popularity = models.IntegerField()
    vote_average = models.FloatField()
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    original_language = models.TextField()
    original_title = models.TextField()
    genre_ids = models.ManyToManyField(Genre)
    backdrop_path = models.TextField()
    adult = models.TextField()
    overview = models.TextField()
    poster_path = models.TextField()

class Rate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="rates")
    rank = models.IntegerField()

class MovieComment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="moviecomments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)