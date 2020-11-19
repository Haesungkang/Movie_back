from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.TextField()

class Movie(models.Model):
    popularity = models.FloatField()
    vote_average = models.FloatField()
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    original_language = models.TextField()
    original_title = models.TextField()
    genre_ids = models.ManyToManyField(Genre)
    # genre_ids = models.TextField()
    # backdrop_path = models.TextField()
    adult = models.TextField()
    overview = models.TextField()
    poster_path = models.TextField()

class Rate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rank = models.IntegerField()