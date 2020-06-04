from rest_framework import serializers
from django.contrib.auth import get_user_model
from taggit.models import Tag
from taggit_serializer.serializers import (TagListSerializerField, TagList,
                                           TaggitSerializer)

from posts.models import Post, Comment


class TagSerializer(TaggitSerializer, serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('name', 'slug')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email')


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'post', 'created')


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'created')
