import datetime
from django.contrib.auth.models import User
from main.models import Category, Product, SubCategory, UserDetail
from .models import LocationStore
from main.models import Shop
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
import math
from django.db.models import Q

# Create your views here.
def getLatLon(request):
    if request.method == "GET":
        query = request.GET['search']

        try:
            user_lat = request.GET['user_latitude']
            user_lon = request.GET['user_longitude']
            user_lat = float(user_lat)
            user_lon = float(user_lon)

            search_postion = []
            queried_shops = []

            search_results = funcSearch(query)
            for i in search_results:
                for j in i:
                    if j is not None:
                        if str(type(j)) == "<class 'main.models.Product'>":
                            search_postion.append({'product':j})
                        if str(type(j)) == "<class 'main.models.Shop'>":
                            search_postion.append({'shop':j})
                        if str(type(j)) == "<class 'main.models.Category'>":
                            search_postion.append({'category':j})
                        if str(type(j)) == "<class 'main.models.SubCategory'>":
                            search_postion.append({'subcategory':j})
                        if str(type(j)) == "<class 'django.contrib.auth.models.User'>":
                            search_postion.append({'user':j})
                        if str(type(j)) == "<class 'main.models.UserDetail'>":
                            search_postion.append({'userdetail':j})

            for i in search_postion:
                if i.get("product") != None:
                    p = i.get("product")
                    queried_shops.append(p.shop)
                if i.get("shop") != None:
                    p = i.get("shop")
                    queried_shops.append(p)

            shops = {}
            for i in queried_shops:
                ls = LocationStore.objects.filter(shop=i).last()
                shop_lat = float(ls.shop_latitude)
                shop_lon = float(ls.shop_longitude)
                distance = CalculateDistance(user_lat,shop_lat,user_lon,shop_lon)
                shops[ls.shop.id] = distance
            # print(shops)
                    
            search_category = []
            search_subcategory = []
            search_user = []
            search_shops = []


            #  This code is to check if the shop is closed or not


            # Note that it will sort in lexicographical order
            # For mathematical way, change it to float
            for i in sorted(shops.items(), key = lambda kv:(kv[1], kv[0])):
                shops = Shop.objects.filter(pk=i[0]).last()
                search_shops.append(shops)


            for i in search_postion:
                for key, value in i.items():
                    if key == "subcategory":
                        search_subcategory.append(SubCategory.objects.filter(pk=value.id).last())
                    if key == "user":
                        search_user.append(UserDetail.objects.filter(user=User.objects.filter(pk=value.id).last()).last())
                    if key == "category":
                        search_category.append(Category.objects.filter(pk=value.id).last())
                    if key == "userdetail":
                        search_user.append(UserDetail.objects.filter(pk=value.id).last())

            context = {'shops':search_shops,'category':search_category, 'subcategory':search_subcategory, 'users':search_user}
            return render(request, "location_manager/search_shops.html", context)
        except:

            search_postion = []
            search_results = funcSearch(query)
            for i in search_results:
                for j in i:
                    if j is not None:
                        if str(type(j)) == "<class 'main.models.Product'>":
                            search_postion.append({'product':j})
                        if str(type(j)) == "<class 'main.models.Shop'>":
                            search_postion.append({'shop':j})
                        if str(type(j)) == "<class 'main.models.Category'>":
                            search_postion.append({'category':j})
                        if str(type(j)) == "<class 'main.models.SubCategory'>":
                            search_postion.append({'subcategory':j})
                        if str(type(j)) == "<class 'django.contrib.auth.models.User'>":
                            search_postion.append({'user':j})
                        if str(type(j)) == "<class 'main.models.UserDetail'>":
                            search_postion.append({'userdetail':j})
            
            search_product = []
            search_shops = []
            search_category = []
            search_subcategory = []
            search_user = []

            for i in search_postion:
                for key, value in i.items():
                    if key == "product":
                        search_product.append(Product.objects.filter(pk=value.id).last())
                    if key == "shop":
                        search_shops.append(Shop.objects.filter(pk=value.id).last())
                    if key == "subcategory":
                        search_subcategory.append(SubCategory.objects.filter(pk=value.id).last())
                    if key == "user":
                        search_user.append(UserDetail.objects.filter(user=User.objects.filter(pk=value.id).last()).last())
                    if key == "category":
                        search_category.append(Category.objects.filter(pk=value.id).last())
                    if key == "userdetail":
                        search_user.append(UserDetail.objects.filter(pk=value.id).last())
            context = {'products':search_product,'shops':search_shops,'category':search_category, 'subcategory':search_subcategory, 'users':search_user}
            return render(request, "location_manager/search_shops.html", context)

def saveLatLon(request,name):
    name = name.replace("-"," ")
    if request.user.is_authenticated:
        if request.method == "POST":
            latitude = request.POST['lat']
            longitude = request.POST['lon']
            shop = Shop.objects.filter(user=request.user, Name=name).last()
            lStore = LocationStore(shop=shop, shop_latitude=latitude, shop_longitude=longitude)
            lStore.save()
            shop = Shop.objects.filter(user=request.user, Name=name).last()
            return HttpResponseRedirect(f"/shopBuilder/{shop.id}")
        return render(request, "location_manager/geolocation.html")
    else:
        return HttpResponseRedirect("/login")

def CalculateDistance(latitude1,latitude2,longitude1,longitude2):
    longDiff = longitude1-longitude2
    distance = math.sin(deg2rad(latitude1))*math.sin(deg2rad(latitude2))+math.cos(deg2rad(latitude1))*math.cos(deg2rad(latitude2))*math.cos(deg2rad(longDiff))

    distance = math.acos(distance);
    distance = rad2deg(distance);

    # distance in Miles
    distance = distance*60*1.1515;
    # Distance in Kilometers
    distance = distance*1.609344;
    return (distance);

def rad2deg(distance):
    return (distance*180.0/math.pi)

def deg2rad(latitude1):
    return (latitude1*math.pi/180.0)

def funcSearch(query):
    # try:
    #     searchQueries(query=query).save()
    # except:
    #     pass

    products = Product.objects.filter(Product_Name__icontains = query)
    categoris = Category.objects.filter(Name__icontains = query)
    subcategoris = SubCategory.objects.filter(Name__icontains = query)
    user = User.objects.filter(Q(username__icontains = query) | Q(first_name__icontains = query) | Q(last_name__icontains = query))
    shops = Shop.objects.filter(Q(Name__icontains = query) | Q(About__icontains = query) | Q(email__icontains = query) | Q(phone__icontains = query), Approved=True)
    userdetails = UserDetail.objects.filter(user_sharable_id__icontains = query)
    
    if products != None:
        if categoris != None:
            if subcategoris != None:
                if user != None:
                    if shops != None:
                        if userdetails != None:
                            return products, shops, categoris, subcategoris, user, userdetails
                        else:
                            return products, shops, categoris, subcategoris, user
                    else:
                        return products, categoris, subcategoris, user
                else:
                    return products, categoris, subcategoris
            else:
                return products, categoris
        else:
            return products


