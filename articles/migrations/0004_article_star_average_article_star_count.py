# Generated by Django 5.0.6 on 2024-05-18 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_rate_ratio_alter_rate_star_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='star_average',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='star_count',
            field=models.IntegerField(default=0),
        ),
    ]
