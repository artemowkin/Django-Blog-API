from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (PostViewSet, UserViewSet, PostsTagList, AuthorPosts,
                    CurrentAuthorPosts, CommentViewSet)

router = SimpleRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('users', UserViewSet, basename='users')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('posts/tag/<slug:slug>/', PostsTagList.as_view()),
    path('users/current/posts/', CurrentAuthorPosts.as_view()),
    path('users/<int:pk>/posts/', AuthorPosts.as_view()),
] + router.urls
