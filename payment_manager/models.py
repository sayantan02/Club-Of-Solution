from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Transaction(models.Model):
    retailer = models.ForeignKey(User, on_delete=models.CASCADE,blank=False,null=False, related_name="retailer")
    collector = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False,related_name="collector")
    trans_id = models.CharField(max_length=14, unique=True)
    balence = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    transaction_completed = models.BooleanField(default=False)
    offer_available = models.BooleanField(default=True)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Retailer: {str(self.retailer)} | Collector: {str(self.collector)}"