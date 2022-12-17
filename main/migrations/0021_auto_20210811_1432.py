# Generated by Django 3.1.1 on 2021-08-11 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20210811_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='user_secret',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='user_sharable_id',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]