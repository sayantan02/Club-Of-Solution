# Generated by Django 3.1.1 on 2021-08-05 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210805_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subcategory'),
        ),
    ]
