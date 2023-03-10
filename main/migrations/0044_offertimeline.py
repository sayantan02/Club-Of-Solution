# Generated by Django 3.1 on 2021-08-26 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_auto_20210821_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferTimeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Offer_Name', models.CharField(max_length=100)),
                ('Product_name', models.CharField(max_length=120)),
                ('text', models.TextField()),
                ('Current_Price', models.IntegerField()),
                ('picture', models.ImageField(upload_to='offers_img')),
                ('Ending_Date', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expired', models.BooleanField(default=False)),
                ('Product_Offer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
        ),
    ]
