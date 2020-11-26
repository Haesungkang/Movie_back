from rest_framework import serializers
from .models import Article, Comment


# 모든 Article의 정보를 반환하기 위한 Serializer
class ArticleListSerializer(serializers.ModelSerializer):

  user_name = serializers.SerializerMethodField()
  def get_user_name(self, obj):
      return obj.user.username

  class Meta:
    model = Article
    # fields = ('id', 'title', 'user', 'created_at', 'content',)
    fields = '__all__'
    read_only_fields = ('user', 'created_at',)


# 모든 Comment의 정보를 반환하기 위한 Serializer
class CommentListSerializer(serializers.ModelSerializer):
  
  user_name = serializers.SerializerMethodField()
  def get_user_name(self, obj):
      return obj.user.username

  class Meta:
    model = Comment
    fields = '__all__'
    # fields = ('id', 'content',)
    read_only_fields = ('user', 'article', 'created_at',)
    

# Article의 상세 정보를 생성 및 반환하기 위한 Serializer
class ArticleSerializer(serializers.ModelSerializer):
  
  user_name = serializers.SerializerMethodField()  
  def get_user_name(self, obj):
      return obj.user.username

  class Meta:
    model = Article
    fields = '__all__'
    # fields = ('id', 'title', 'content', 'user',)
    read_only_fields = ('user',)


# Comment의 상세 정보를 생성 및 반환하기 위한 Serializer
class CommentSerializer(serializers.ModelSerializer):

  user_name = serializers.SerializerMethodField()
  def get_user_name(self, obj):
      return obj.user.username
  
  class Meta:
    model = Comment
    fields = '__all__'
    # fields = ('id', 'content', 'article',)
    read_only_fields = ('user', 'article',)