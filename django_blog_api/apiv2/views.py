from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        IsAuthenticated)
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.http import Http404
from django.db.models import Q
from taggit.models import Tag

from posts.models import Post, Comment
from .serializers import (PostSerializer, UserSerializer, CommentSerializer,
                          TagSerializer)
from .permissions import IsAuthorOrReadOnly


class PostCommentsViewSet(ModelViewSet):
    """
    retrieve:
        Return comment of the post

    list:
        Return the comments list of the post

    create:
        Create a new comment of the post

    update:
        Update the given comment of the post

    partial_update:
        Update the given comment of the post

    delete:
        Delete the given comment
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.filter(deleted=False)
    serializer_class = CommentSerializer

    def get_queryset(self):
        return super().get_queryset().filter(
            post__pk=self.kwargs.get('post_pk')
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.deleted = True
        obj.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostTagsViewSet(ModelViewSet):
    """
    retrieve:
        Return given tag of the post

    list:
        Return the tags list of the post

    create:
        Create a new tag of the post

    update:
        Update the given tag of the post

    partial_update:
        Update the given tag of the post

    delete:
        Delete the given tag of the post
    """
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        post = Post.objects.get(pk=self.kwargs.get('post_pk'))
        return post.tags.all()


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


class PostsFilterByTag(ListAPIView):
    """
    Return the list of blog posts with the given tag's slug
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(tags__slug=self.kwargs.get('tag_slug'))


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


class TagsList(ListAPIView):
    """
    Return the list of all tags
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostSearchView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            raise Http404

        return super().get_queryset().filter(
            Q(title__icontains=query) | Q(author__username__icontains=query)
        )
