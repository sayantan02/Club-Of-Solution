# Generated by Django 3.1.1 on 2021-08-14 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_manager', '0003_auto_20210814_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='trans_id',
            field=models.CharField(max_length=14),
        ),
    ]
