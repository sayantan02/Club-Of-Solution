# Generated by Django 3.1.1 on 2021-08-21 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_contact_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]
