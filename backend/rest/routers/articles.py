from rest_framework import routers

from rest.viewsets.articles import FeedViewSet, CreateArticleViewSet, UpdateArticleViewSet
from rest.viewsets.tags import TagsViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'feed', FeedViewSet, basename="feed")
router.register(r'article', CreateArticleViewSet, basename='article')
router.register(r'article_change', UpdateArticleViewSet, basename='article')
router.register(r'tag', TagsViewSet, basename='tag')
