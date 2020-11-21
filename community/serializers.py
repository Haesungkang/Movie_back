from rest_framework import serializers
from .models import Article, Comment

class ArticleSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Article
    fields = ('id', 'title', 'content',)


class CommentSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Comment
    fields = ('id', 'content',)