from django.db import models
from main.models import Shop

# Create your models here.
class CountView(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    view_count = models.IntegerField(default=0)
    last_updated = models.TimeField(auto_now=True)
    date = models.DateField(auto_now_add=True)
