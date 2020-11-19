from django.urls import path
from . import views

# app_name = 'movie_info'

urlpatterns = [
    path('', views.index),
]