from articles.models import Rate
from datetime import timedelta
from django.utils import timezone


def find_influenced_rates(article_id):
	time_threshold = 30
	start_time = timezone.now() - timedelta(seconds=time_threshold)
	star_average = Rate.objects.aggregate(weighted_avg=Avg(F('rate__star') * F('rate__ratio')))['weighted_avg'] / 100
	recent_rates = Rate.objects.filter(article_id=article_id, timestamp__gte=time_limit)

	# TODO: Make these variables dynamic
	x = 5
	y = 0

	if influenced_rates := recent_rates.filter(star__gt=star_average + y).count() >= x:
		change_influenced_rates_ratio(influenced_rates)

	if influenced_rates := recent_rates.filter(star__lt=star_average - y).count() >= x:
		change_influenced_rates_ratio(influenced_rates)

def change_influenced_rates_ratio(rates):
	z = rates.count()
	for rating in recent_rates:
		rating.score /= z
		rating.save()

