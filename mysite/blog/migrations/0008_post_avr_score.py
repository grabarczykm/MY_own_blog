# Generated by Django 2.0.6 on 2018-06-30 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180629_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='avr_score',
            field=models.FloatField(default=0.0),
        ),
    ]
