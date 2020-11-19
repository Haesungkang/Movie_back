from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.shortcuts import render, get_object_or_404
from .models import Movie
from .serializers import MovieSerializer

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)