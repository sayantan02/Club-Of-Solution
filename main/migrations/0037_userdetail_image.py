# Generated by Django 3.1.1 on 2021-08-14 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_userdetail_payment_initialized'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='protfolio_image'),
        ),
    ]