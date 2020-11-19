from django.db import models

# Create your models here.
class Recommend(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()