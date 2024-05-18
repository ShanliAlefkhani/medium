from django.db import models
from django.db.models import Avg, F
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from timestampedmodel import TimestampedModel
from django.db.models.signals import post_save
from django.dispatch import receiver


class Article(TimestampedModel):
	title = models.CharField(max_length=100)
	ratings = models.ManyToManyField(User, through='Rate')
	star_count = models.IntegerField(default=0)
	star_average = models.FloatField(default=0)

	@property
	def ratings_average(self):
		weighted_avg = self.ratings.aggregate(weighted_avg=Avg(F('rate__star') * F('rate__ratio')))['weighted_avg']
		return weighted_avg / 100 if weighted_avg else 0

class Rate(TimestampedModel):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	star = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
	ratio = models.IntegerField(default=100, validators=[MinValueValidator(0), MaxValueValidator(100)])

	class Meta:
		unique_together = ('article', 'user')

@receiver(post_save, sender=Rate)
def rate_post_save_handler(sender, instance, created, **kwargs):
	if created:
		article = instance.article
		article.star_average = ((article.star_average * article.star_count) + int(instance.star)) / (article.star_count + 1)
		article.star_count += 1
		article.save()

