from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (PostViewSet, UserViewSet, PostsFilterByTag, AuthorPosts,
                    CurrentAuthorPosts, PostCommentsViewSet, TagsList,
                    PostTagsViewSet, PostSearchView)

router = SimpleRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('posts/(?P<post_pk>[^/.]+)/comments', PostCommentsViewSet,
                basename='posts_comments')
router.register('posts/(?P<post_pk>[^/.]+)/tags', PostTagsViewSet,
                basename='posts_tags')
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('posts/filter/<slug:tag_slug>/', PostsFilterByTag.as_view()),
    path('posts/search/', PostSearchView.as_view()),
    path('users/current/posts/', CurrentAuthorPosts.as_view()),
    path('users/<int:pk>/posts/', AuthorPosts.as_view()),
    path('tags/', TagsList.as_view()),
] + router.urls
