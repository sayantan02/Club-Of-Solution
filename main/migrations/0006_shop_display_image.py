# Generated by Django 3.1.1 on 2021-08-05 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_subcategory_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='Display_Image',
            field=models.ImageField(default='CatImage/default.jpg', upload_to='shopDP'),
        ),
    ]