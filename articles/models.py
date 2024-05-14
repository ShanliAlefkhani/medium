from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User

class Article(models.Model):
	title = models.CharField(max_length=100)
	ratings = models.ManyToManyField(User, through='Rate')

	@property
	def number_of_users_rated(self):
		return self.ratings.count()

	@property
	def ratings_average(self):
		print(self.ratings.aggregate(Avg('rate__star')).get('rate__star__avg'))
		return self.ratings.aggregate(Avg('rate__star')).get('rate__star__avg')

class Rate(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	star = models.IntegerField()

