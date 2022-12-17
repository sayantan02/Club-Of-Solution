from admin_panel.models import CountView
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Shop, ShopView, UserDetail, Member


@receiver(post_save, sender=User)
def save_UserDetails(sender, instance, created, **kwarg):
    if created:
        UserDetail.objects.create(user=instance)

@receiver(post_save,sender=Shop)
def saveShopView(sender, instance, created, **kwarg):
    if created:
        ShopView.objects.create(shop=instance)

@receiver(post_save,sender=Shop)
def saveMember(sender, instance, created, **kwarg):
    if created:
        Member.objects.create(shop=instance)

@receiver(post_save,sender=Shop)
def createView(sender, instance, created, **kwarg):
    if created:
        CountView.objects.create(shop=instance)
