# Generated by Django 4.1.2 on 2022-11-05 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aligulacv2', '0004_match_history_player_a_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match_history',
            name='player_a_rating',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='match_history',
            name='player_a_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='match_history',
            name='player_b_rating',
            field=models.IntegerField(default=10),
        ),
    ]
