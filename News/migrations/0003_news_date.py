# Generated by Django 4.1.5 on 2023-01-27 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_subscribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
