from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.shortcuts import render, get_object_or_404

from rest_framework import status
from .serializers import MovieSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Movie, MovieComment
from .serializers import MovieCommentSerializer
# Create your views here.

@api_view(['GET'])
def nowplaying(request):
    # 영화 목록을 추가할 필요는 없으므로 GET 방식만 가능하도록 설정한다.
    # if request.method == 'GET':
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_comment_list(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comments = movie.moviecomments.all()
    serializer = MovieCommentSerializer(comments, many=True)
    return Response(serializer.data)