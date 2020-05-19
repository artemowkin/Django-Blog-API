from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model
from taggit.models import Tag

from posts.models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserViewSet(ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class PostsTagList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(tags__slug=self.kwargs.get('slug'))


class AuthorPosts(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(author__id=self.kwargs.get('pk'))
