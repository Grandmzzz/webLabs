from rest_framework import serializers

from articles.models import Article


class FeedArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class CreateArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ['image', 'date_create']


class UpdateArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ['image', 'author', 'date_create']
