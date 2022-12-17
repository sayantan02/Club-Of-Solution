from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('login/',views.Login,name="login"),
    path('logout',views.Logout,name="logout"),
    path('about/',views.about,name="about"),
    path('contact/<str:position>/',views.contact,name="contact"),
    path('addshop/',views.addshop,name="addshop"),
    path('addcat/',views.addcat,name="addcat"),
    path('addproduct/',views.addproduct,name="addproduct"),
    path('addcategory/',views.addcategory,name="addcategory"),
    path('adddirectshop/',views.adddirectshop,name="adddirectshop"),
    path('shops/<str:cat_slug>/<int:id>/',views.Shops,name="shops"),
    path('shopview/<int:shop>/',views.shopView,name="shopview"),
    path('shopBuilder/<int:shop>/',views.shopBuilder,name="shopBuilder"),
]
