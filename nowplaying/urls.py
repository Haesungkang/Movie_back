from django.urls import path
from . import views

urlpatterns = [
    path('', views.nowplaying),
    path('<int:movie_pk>/comment_list/', views.movie_comment_list),
    path('<int:movie_pk>/comments/', views.movie_comment_create),
]