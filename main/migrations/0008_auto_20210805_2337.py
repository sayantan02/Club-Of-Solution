# Generated by Django 3.1.1 on 2021-08-05 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_auto_20210805_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='Items',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
