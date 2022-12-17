from django.db import models
from main.models import Shop

# Create your models here.
class LocationStore(models.Model):
    Name = models.CharField(max_length=200,blank=True,null=True, unique=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True, null=True)
    shop_latitude = models.CharField(max_length=200)
    shop_longitude = models.CharField(max_length=200)

class LocationStoreUser(models.Model):
    user_latitude = models.CharField(max_length=200)
    user_longitude = models.CharField(max_length=200)

# class searchQueries(models.Model):
#     query = models.TextField(unique=True)
#     datetime = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.query
