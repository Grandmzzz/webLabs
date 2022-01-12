from rest_framework import viewsets, permissions

from articles.models import Tag
from rest.serializers.tags import TagSerializer


class TagsViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    http_method_names = ["get", "post", "patch", "delete"]
