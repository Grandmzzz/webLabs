from django.db.models import Q
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import IN_QUERY, Parameter, TYPE_STRING, TYPE_INTEGER
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from rest.serializers.articles import FeedArticleSerializer, CreateArticleSerializer, UpdateArticleSerializer

from articles.models import Article, Tag


class FeedViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Article.objects.all()
    serializer_class = FeedArticleSerializer
    http_method_names = ["get"]

    @swagger_auto_schema(
        operation_description="Поиск по тексту",
        manual_parameters=[
            Parameter(
                "search_text",
                IN_QUERY,
                description="Строка для поиска",
                type=TYPE_STRING
            )],
        responses={
            200: FeedArticleSerializer(many=True)
        }
    )
    @action(methods=["get"], detail=False)
    def by_text(self, request):
        search_text = request.query_params.get("search_text", '')

        articles = Article.objects.filter(
            Q(title__contains=search_text) |
            Q(description__contains=search_text) |
            Q(text__contains=search_text)
        )

        serializer = FeedArticleSerializer(articles, many=True)

        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Поиск по тегу",
        manual_parameters=[
            Parameter(
                "tag_id",
                IN_QUERY,
                description="ID тега по которому идет поиск",
                type=TYPE_INTEGER
            )],
        responses={
            200: FeedArticleSerializer(many=True),
            404: "Нет такого тега"
        }
    )
    @action(methods=["get"], detail=False)
    def by_tag(self, request):
        tag_id = request.query_params.get("tag_id", None)

        tag = get_object_or_404(Tag, id=tag_id)
        articles = tag.article_set.all()

        serializer = FeedArticleSerializer(articles, many=True)

        return Response(serializer.data)


class CreateArticleViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = CreateArticleSerializer
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        request.data["author"] = request.user.id
        return super().create(request, *args, **kwargs)


class UpdateArticleViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = UpdateArticleSerializer
    http_method_names = ["patch", 'delete']
