# Generated by Django 3.1.1 on 2021-08-13 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_manager', '0004_searchqueries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchqueries',
            name='query',
            field=models.TextField(unique=True),
        ),
    ]
