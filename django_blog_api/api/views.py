from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        IsAuthenticated)
from django.contrib.auth import get_user_model
from taggit.models import Tag

from posts.models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(ModelViewSet):
    """
    retrieve:
        Return the giving blog post

    list:
        Return the list of blog posts

    create:
        Create a new blog post

    update:
        Update the given blog post
partial_update:
        Update the given fields of the post

    delete:
        Delete the given post
    """
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserViewSet(ReadOnlyModelViewSet):
    """
    retrieve:
        Return the giving user

    list:
        Return the list of existing users
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class PostsTagList(ListAPIView):
    """
    Return the list of blog posts with the given tag's slug
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(tags__slug=self.kwargs.get('slug'))


class AuthorPosts(ListAPIView):
    """
    Return the list of user's posts
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(author__id=self.kwargs.get('pk'))


class CurrentAuthorPosts(ListAPIView):
    """
    Return the list of current user's posts
    """
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)
