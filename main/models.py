
from django.db import models
from django.contrib.auth.models import User


# class CustomDateTimeField(models.DateTimeField):
#     def value_to_string(self, obj):
#         val = self.value_from_object(obj)
#         if val:
#             val.replace(microsecond=0)
#             return val.isoformat()
#         return ''

class UserDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_sharable_id = models.CharField(max_length=20, unique=True,blank=True,null=True)
    user_secret = models.CharField(max_length=50, unique=True,blank=True,null=True)
    image = models.ImageField(upload_to="protfolio_image", blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    is_cafe = models.BooleanField(default=False)
    cafe_secret_key = models.CharField(max_length=50,blank=True,null=True)
    payment_succeed = models.BooleanField(default=False)
    payment_initialized = models.BooleanField(default=False)
    location_succeed = models.BooleanField(default=False)
    is_half_kyc_verified = models.BooleanField(default=False)
    is_full_kyc_verified = models.BooleanField(default=False)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

# Should Be Removed
class Category(models.Model):
    Name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.Name

class SubCategory(models.Model):
    Name = models.CharField(max_length=80, unique=True)
    Sub = models.ForeignKey(Category, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='CatImage', default='CatImage/default.jpg')
    Items = models.IntegerField(default=0)
    slug = models.SlugField()

    def __str__(self):
        return self.Name+" ---> "+str(self.Sub.Name)
    
class Shop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_details = models.ForeignKey(UserDetail, on_delete=models.CASCADE,blank=True,null=True)
    Name = models.CharField(max_length=100, unique=True)
    About = models.CharField(max_length=200)
    Display_Image = models.ImageField(upload_to="shopDP",default="CatImage/default.jpg")
    opening = models.TimeField()
    closing = models.TimeField()
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    cat = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    location = models.TextField()
    is_verified = models.BooleanField(default=False)
    products_added = models.IntegerField(default=0)
    Approved = models.BooleanField(default=False)
    Cancelled = models.BooleanField(blank=True, default=False)
    Created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name+" --> "+self.city

class ShopView(models.Model):
    # Images = models.ForeignKey(Shop_Img, on_delete=models.CASCADE, blank=True, null=True)
    shop   = models.OneToOneField(Shop, on_delete=models.CASCADE)
    slider1 = models.ImageField(upload_to="shopviewImg",blank=True,null=True)
    slider2 = models.ImageField(upload_to="shopviewImg",blank=True,null=True)
    slider3 = models.ImageField(upload_to="shopviewImg",blank=True,null=True)
    slider4 = models.ImageField(upload_to="shopviewImg",blank=True,null=True)
    shop_type = models.CharField(max_length=100,blank=True,null=True)
    about_sitution = models.IntegerField(blank=True,null=True)
    about = models.CharField(max_length=200)

    def __str__(self):
        return str(self.shop)

class Contact(models.Model):
    Username = models.CharField(max_length=200)
    Name = models.CharField(max_length=80)
    phone = models.CharField(max_length=100)
    Reason = models.CharField(max_length=150)
    Describe = models.TextField()
    Sended_at = models.DateTimeField(auto_now_add=True)
    viewed = models.BooleanField(default=False)
    user_viewed = models.BooleanField(default=False)

    def __str__(self):
        return self.Reason

class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    Product_Name = models.CharField(max_length=120)
    # Product_Image = models.ImageField(upload_to="product_image")
    Product_M_R_P = models.IntegerField()
    # Product_Price = models.IntegerField()
    # Specifications = models.TextField()
    # About_Product = models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Product_Name+" --- "+str(self.shop)

    class Meta:
        ordering = ("-added",)

class OfferTimeline(models.Model):
    Offer_Name = models.CharField(max_length=100)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    Product_Offer = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True , null=True)
    Product_name = models.CharField(max_length=120, blank=True , null=True)
    text = models.TextField()
    Current_Price = models.IntegerField()
    picture = models.ImageField(upload_to="offers_img")
    Ending_Date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    expired = models.BooleanField(default=False)

    def __str__(self):
        return self.Offer_Name

    class Meta:
        ordering = ('-created',)

# class ProductReview(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
#     review = models.IntegerField()
#     message = models.TextField()

#     def __str__(self):
#         return self.user.username+" -- "+str(self.review)

class PopularItem1(models.Model):
    item_name = models.CharField(max_length=100)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.shop)

class PopularItem2(models.Model):
    item_name = models.CharField(max_length=100)
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.shop)

class PopularItem3(models.Model):
    item_name = models.CharField(max_length=100)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.shop)

class Member(models.Model):
    shop = models.OneToOneField(Shop, on_delete=models.CASCADE)
    user1 = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name="employee1", blank=True, null=True)
    user2 = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name="employee2", blank=True, null=True)
    user3 = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name="employee3", blank=True, null=True)
    user4 = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name="employee4", blank=True, null=True)
    user5 = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name="employee5", blank=True, null=True)
    user6 = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name="employee6", blank=True, null=True)
    user7 = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name="employee7", blank=True, null=True)
    user8 = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name="employee8", blank=True, null=True)
    user9 = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name="employee9", blank=True, null=True)
    user10 = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name="employee10", blank=True, null=True)
    user11 = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name="employee11", blank=True, null=True)
    user12 = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name="employee12", blank=True, null=True)
    user13 = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name="employee13", blank=True, null=True)
    user14 = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name="employee14", blank=True, null=True)
    user15 = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name="employee15", blank=True, null=True)
    user16 = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name="employee16", blank=True, null=True)
    user17 = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name="employee17", blank=True, null=True)
    user18 = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name="employee18", blank=True, null=True)
    user19 = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name="employee19", blank=True, null=True)
    user20 = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name="employee20", blank=True, null=True)

    def __str__(self):
        return str(self.shop.Name)




