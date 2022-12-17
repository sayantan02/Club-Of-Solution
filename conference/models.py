from django.db import models
from main.models import Shop, UserDetail

# Create your models here.
class ConferenceRoom(models.Model):
    user = models.ForeignKey(UserDetail, on_delete= models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete= models.CASCADE, null= True, blank= True)
    code = models.CharField(max_length= 20, unique= True)
    name = models.CharField(max_length= 100, null= True, blank= True)
    datetime = models.DateTimeField(auto_now_add= True)

    class Meta:
        ordering = ("-datetime",)