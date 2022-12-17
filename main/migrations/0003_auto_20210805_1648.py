# Generated by Django 3.1.1 on 2021-08-05 11:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210805_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='Created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shop',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
