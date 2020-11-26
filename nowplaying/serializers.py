from rest_framework import serializers
from .models import Movie, MovieComment

class MovieSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Movie
    fields = '__all__'
  

class MovieCommentSerializer(serializers.ModelSerializer):

  user_name = serializers.SerializerMethodField()
  def get_user_name(self, obj):
      return obj.user.username
  
  class Meta:
    model = MovieComment
    fields = '__all__'
    # fields = ('id', 'content', 'article',)
    read_only_fields = ('user', 'movie', 'created_at', 'updated_at',)