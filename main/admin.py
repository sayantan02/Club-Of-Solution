from django.contrib import admin
from .models import Member, OfferTimeline, PopularItem1, PopularItem2, PopularItem3, Product, SubCategory, Category, Shop, ShopView, Contact, UserDetail
# Register your models here.

admin.site.register(UserDetail)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Shop)
admin.site.register(ShopView)
admin.site.register(Contact)
admin.site.register(Product)
# admin.site.register(ProductReview)
admin.site.register(PopularItem1)
admin.site.register(PopularItem2)
admin.site.register(PopularItem3)
admin.site.register(Member)
admin.site.register(OfferTimeline)