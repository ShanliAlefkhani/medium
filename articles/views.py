from rest_framework import generics
from articles.models import Article
from articles.serializers import ArticleSerializer


class ArticleList(generics.ListAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

