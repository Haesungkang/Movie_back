from rest_framework import serializers
from .models import Article, Comment


# 모든 Article의 정보를 반환하기 위한 Serializer
class ArticleListSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Article
    fields = ('id', 'title',)


# 모든 Comment의 정보를 반환하기 위한 Serializer
class CommentListSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Comment
    fields = ('id', 'content',)
    

# Article의 상세 정보를 생성 및 반환하기 위한 Serializer
class ArticleSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Article
    fields = ('id', 'title', 'content',)


# Comment의 상세 정보를 생성 및 반환하기 위한 Serializer
class CommentSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Comment
    fields = ('id', 'content', 'article',)
    read_only_fields = ('article',)