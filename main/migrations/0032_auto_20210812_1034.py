# Generated by Django 3.1.1 on 2021-08-12 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20210812_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='About',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='shopview',
            name='about',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
