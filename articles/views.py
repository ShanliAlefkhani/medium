from rest_framework import generics, status
from articles.models import Article, Rate
from articles.serializers import ArticleSerializer, RateSerializer
from rest_framework.response import Response


class ArticleList(generics.ListAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

class RateCreate(generics.CreateAPIView):
	queryset = Rate.objects.all()
	serializer_class = RateSerializer

	def create(self, request, *args, **kwargs):
		rate, created = Rate.objects.update_or_create(
			user=request.user,
			defaults={'star': request.data.get('star')}
		)
		serializer = self.get_serializer(rate)
		return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

