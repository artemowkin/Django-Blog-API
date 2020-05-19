from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, UserViewSet, PostsTagList, AuthorPosts

router = SimpleRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('posts/tag/<slug:slug>/', PostsTagList.as_view()),
    path('users/<int:pk>/posts/', AuthorPosts.as_view()),
] + router.urls
