from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from rest.routers.static_data import router as router_static_data
from rest.routers.auth import router as router_auth
from rest.routers.articles import router as router_articles

schema_view = get_schema_view(
    openapi.Info(
        title="MAGAZINE API",
        default_version='v1',
        description="Полный список api",
    ),
    patterns=[
        path('api/', include('rest.urls')),
    ],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('static_data/', include(router_static_data.urls)),
    path('auth/', include(router_auth.urls)),
    path('articles/', include(router_articles.urls))
]
