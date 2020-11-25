from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.shortcuts import render, get_object_or_404
from .models import Movie
from .serializers import MovieSerializer

# Create your views here.
@api_view(['GET'])
def nowplaying(request):
    # 영화 목록을 추가할 필요는 없으므로 GET 방식만 가능하도록 설정한다.
    # if request.method == 'GET':
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)