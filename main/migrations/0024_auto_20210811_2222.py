# Generated by Django 3.1.1 on 2021-08-11 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_shopview_about_sitution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopview',
            name='about_sitution',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
