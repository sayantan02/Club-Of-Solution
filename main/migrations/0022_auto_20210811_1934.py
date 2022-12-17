# Generated by Django 3.1.1 on 2021-08-11 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20210811_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopview',
            old_name='code',
            new_name='about',
        ),
        migrations.RemoveField(
            model_name='shopview',
            name='Images',
        ),
        migrations.RemoveField(
            model_name='shopview',
            name='code1',
        ),
        migrations.RemoveField(
            model_name='shopview',
            name='code2',
        ),
        migrations.RemoveField(
            model_name='shopview',
            name='code3',
        ),
        migrations.AddField(
            model_name='shopview',
            name='shop_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shopview',
            name='slider1',
            field=models.ImageField(blank=True, null=True, upload_to='shopviewImg'),
        ),
        migrations.AddField(
            model_name='shopview',
            name='slider2',
            field=models.ImageField(blank=True, null=True, upload_to='shopviewImg'),
        ),
        migrations.AddField(
            model_name='shopview',
            name='slider3',
            field=models.ImageField(blank=True, null=True, upload_to='shopviewImg'),
        ),
        migrations.AddField(
            model_name='shopview',
            name='slider4',
            field=models.ImageField(blank=True, null=True, upload_to='shopviewImg'),
        ),
        migrations.DeleteModel(
            name='Shop_Img',
        ),
    ]
