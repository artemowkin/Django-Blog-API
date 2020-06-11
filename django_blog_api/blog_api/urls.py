from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version="v2",
        description="Our first Blog REST API",
        license=openapi.License(name='GPL-3.0'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # API version 1
    path('api/v1/', include('api.urls')),
    path('api/v1/auth/', include('dj_rest_auth.urls')),
    path('api/v1/auth/registration/',
         include('dj_rest_auth.registration.urls')),

    # API version 2
    path('api/v2/', include('apiv2.urls')),
    path('api/v2/auth/', include('dj_rest_auth.urls')),
    path('api/v2/auth/registration/',
         include('dj_rest_auth.registration.urls')),

    # Docs
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0)),

    # Local apps
    path('', include('posts.urls')),
]
