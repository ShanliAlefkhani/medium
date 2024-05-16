from rest_framework import serializers
from articles.models import Article, Rate


class ArticleSerializer(serializers.ModelSerializer):
	number_of_users_rated = serializers.ReadOnlyField()
	ratings_average = serializers.ReadOnlyField()
	user_rate = serializers.SerializerMethodField()

	def get_user_rate(self, obj):
		request = self.context.get('request')
		if request and request.user.is_authenticated:
			user = request.user
			try:
				rate = Rate.objects.get(article=obj, user=user)
				return rate.star
			except Rate.DoesNotExist:
				return None
		return None

	class Meta:
		model = Article
		fields = ['title', 'number_of_users_rated', 'ratings_average', 'user_rate']

class RateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rate
		fields = ['article', 'star']
