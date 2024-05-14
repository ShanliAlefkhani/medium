from rest_framework import serializers
from articles.models import Article, Rate


class RateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rate
		fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
	ratings = RateSerializer(source='rate_set', many=True)
	number_of_users_rated = serializers.ReadOnlyField()
	ratings_average = serializers.ReadOnlyField()

	class Meta:
		model = Article
		fields = '__all__'

