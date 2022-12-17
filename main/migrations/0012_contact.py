# Generated by Django 3.1.1 on 2021-08-07 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210806_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=80)),
                ('Contact', models.CharField(max_length=16)),
                ('Reason', models.CharField(max_length=150)),
                ('Describe', models.TextField()),
                ('Sended_at', models.DateTimeField(auto_now_add=True)),
                ('viewed', models.BooleanField(default=False)),
            ],
        ),
    ]