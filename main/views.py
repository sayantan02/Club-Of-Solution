# from location_manager.models import searchQueries
from location_manager.models import LocationStore
from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Member, OfferTimeline, PopularItem1, PopularItem2, PopularItem3, Product, SubCategory, Category, Shop, ShopView, Contact, UserDetail
from django.contrib.auth import authenticate, logout, login
from datetime import date, datetime

# Create your views here.
def index(request):
    subcategory = SubCategory.objects.all()
    category = Category.objects.all()
    item1 = PopularItem1.objects.all()
    item2 = PopularItem2.objects.all()
    item3 = PopularItem3.objects.all()
    products = Product.objects.all()
    # queryes = searchQueries.objects.all()
    # queries = []

    # for i in queryes:
    #     queries.append(i.query)
    # for i in products:
    #     queries.append(i.Product_Name)

    context = {'sub_category':subcategory,'category':category, 'item_1':item1, 'item_2':item2, 'item_3':item3}
    return render(request, "main/index.html",context)

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if request.method == "POST":
            user_name = request.POST['username']
            Name = request.POST['name']
            Mail = request.POST['email']
            password_1 = request.POST['pass_1']
            password_2 = request.POST['pass_2']

            if (password_1 != password_2):
                return render(request, "main/register.html",{'refused':True, 'message':'passwords did no matched'})
            if (len(password_1) < 10):
                return render(request, "main/register.html",{'refused':True, 'message':'Password must be atleast 10 words'})

            name = Name.split(" ")
            if(not name[1]):
                name1 = Name.split("  ")
                try:
                    user = User.objects.create_user(user_name, Mail, password_2)
                    user.first_name = name1[0]
                    user.last_name = name[1]
                    user.save()
                    # return HttpResponseRedirect("/Admin/user/Dashboard")
                except:
                    return render(request, "main/register.html",{'refused':True})
            try:
                user = User.objects.create_user(user_name,Mail,password_2)
                user.first_name = name[0]
                user.last_name = name[1]
                user.save()
            except:
                return render(request, "main/register.html",{'refused':True})

            user_auth = authenticate(username=user_name,password=password_2)
            if user_auth is not None:
                login(request,user_auth)
            return HttpResponseRedirect("/payment_manager/payment")

        return render(request, "main/register.html")

def about(request):
    return render(request, "main/about.html")

def contact(request,position):
    if request.method == "POST":
        Username = request.POST['username']
        Name = request.POST['name']
        number = request.POST['contact']
        Reason = request.POST['reason']
        Describe = request.POST['message']
        cont = Contact(Username=Username, Name=Name, phone=number, Reason=Reason, Describe=Describe)
        cont.save()
        if position == "admin":
            return HttpResponseRedirect("/Admin/user/Dashboard")
        else:
            return render(request, "main/contact.html", {'success':True})
    return render(request, "main/contact.html")

def Login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if request.method == "POST":
            cred = request.POST['credential']
            password = request.POST['pass']
            user = authenticate(username=cred, password=password)
            if user is not None:
                login(request,user)

                if UserDetail.objects.filter(user=request.user, payment_initialized=False):
                    return HttpResponseRedirect("/payment_manager/payment")
                else:
                    print("else printed")
                    return HttpResponseRedirect("/Admin/user/Dashboard")
    return render(request, "main/login.html")

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def addshop(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            Name = request.POST['name'] 
            About = request.POST['about']
            Display_Image = request.FILES['image']
            Opening = request.POST['opening']
            Closing = request.POST['closing']
            Email = request.POST['email'] 
            Phone = request.POST['phone']
            City = request.POST['city']
            cat = request.POST['category']
            location = request.POST['loc']


            f_cat = SubCategory.objects.filter(pk=cat).first()
            try:
                add_shop = Shop(user=request.user, user_details=UserDetail.objects.filter(user=request.user).last(), Name=Name, About=About, Display_Image=Display_Image, opening=Opening, closing=Closing, email=Email, phone=Phone, city=City, cat=f_cat, location=location)
                add_shop.save()
                f_cat.Items = f_cat.Items+1
                f_cat.save()
            except:
                return render(request, "main/addshop.html",{'refused':True})
            category = SubCategory.objects.all()
            context = {'category':category,'success':True}
            send_name = Name.replace(" ","-")
            return HttpResponseRedirect(f"/location_manager/savelatlon/{send_name}")
            # except:
            #     return render(request, "main/addshop.html",{'refused':True})
        else:
            category = SubCategory.objects.all()
            context = {'category':category}
            return render(request, "main/addshop.html",context)
    else:
        return HttpResponseRedirect("/login")

def addcat(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST['Name']
            sub = request.POST['category']
            image = request.FILES['image']
            if SubCategory.objects.filter(Name=name):
                # Returning
                cats = Category.objects.all()
                context = {'cat':cats,'refused':True}
                return render(request, "main/addcat.html",context)
            else:
                slug = name.replace(" ","-")
                cat = Category.objects.filter(pk=sub).last()
                try:
                    subCategory = SubCategory(Name=name,Sub=cat,Image=image,slug=slug)
                    subCategory.save()
                except:
                    return render(request, "main/addcat.html",{'refused':False})
                # Returning
                cats = Category.objects.all()
                context = {'cat':cats,'success':True}
                return render(request, "main/addcat.html",context)
        
        cats = Category.objects.all()
        context = {'cat':cats}
        if request.user.is_superuser:
            return render(request, "main/addcat.html",context)
        else:
            return HttpResponse("You don not have Previllages to access this page")
    else:
        return HttpResponseRedirect("/login")

def Shops(request,cat_slug,id):
    shops = Shop.objects.filter(cat=SubCategory.objects.filter(pk=id).last())
    context = {'shops':shops,'search':cat_slug}
    return render(request,"main/shops.html",context)

def shopView(request,shop):
    shop_view = ShopView.objects.filter(shop=Shop.objects.filter(pk=shop).last()).first()
    Offers = OfferTimeline.objects.filter(shop=Shop.objects.filter(pk=shop).last())
    members = Member.objects.filter(shop=Shop.objects.filter(pk=shop).last()).last()
    now = datetime.now()
    ct = now.strftime("%H:%M:%S")
    shops = Shop.objects.filter(pk=shop).last()
    ot = shops.opening
    clt = shops.closing

    ot = str(ot)
    clt = str(clt)

    current_time = ct.split(":")
    opening_time = ot.split(":")
    closing_time = clt.split(":")

    opened = False
    closed = False

    if current_time[0] > opening_time[0]: # checking hour
        if current_time[0] < closing_time[0]: # checking hour
            opened = True
        elif current_time[0] == closing_time[0]: # checking hour
            if current_time[1] < closing_time[1]: # checking minutes
                opened = True
            else:
                closed = True
        else:
            closed = True
    elif current_time[0] == opening_time[0]: # checking hour
        if current_time[1] > opening_time[1]: # checking minutes
            opened = True
        elif current_time[1] == opening_time[1]: # checking minutes
            opened = True
        else:
            closed = True
    else:
        closed = True

    if not shop_view:
        return render(request,"page404.html")
    context = {'shop_view':shop_view, 'members':members, 'opened':opened, 'closed':closed,'offers':Offers}
    return render(request,"main/shop_profile.html",context)

def shopBuilder(request,shop):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST['username']
            username = User.objects.filter(username=name).last()
            t_shop = Shop.objects.filter(pk=shop).last()
            if not t_shop.user == username:
                return render(request, "main/shop_builder.html", {'refused':True})
            create_view = ShopView.objects.filter(shop=t_shop).first()

            slider_1 = request.FILES['slide1']
            slider_2 = request.FILES['slide2']
            slider_3 = request.FILES['slide3']
            slider_4 = request.FILES['slide4']
            s_type = request.POST['shop_type']
            about_sitution = request.POST['about']
            if about_sitution == "About":
                create_view.slider1 = slider_1
                create_view.slider2 = slider_2
                create_view.slider3 = slider_3
                create_view.slider4 = slider_4
                create_view.shop_type = s_type
                create_view.about_sitution = 1
                create_view.save()
            elif about_sitution == "type-own":
                about_text = request.POST['abouttext']
                create_view.slider1 = slider_1
                create_view.slider2 = slider_2
                create_view.slider3 = slider_3
                create_view.slider4 = slider_4
                create_view.shop_type = s_type
                create_view.about_sitution = 1
                create_view.about = about_text
                create_view.save()
                
            emp1 = ""
            emp2 = ""
            emp3 = ""
            emp4 = ""
            emp5 = ""
            emp6 = ""
            emp7 = ""
            emp8 = ""
            emp9 = ""
            emp10 = ""
            emp11 = ""
            emp12 = ""
            emp13 = ""
            emp14 = ""
            emp15 = ""
            emp16 = ""
            emp17 = ""
            emp18 = ""
            emp19 = ""
            emp20 = ""

            try:
                emp1 = request.POST['emp1']
            except:
                pass 

            try:
                emp2 = request.POST['emp2']
            except:
                pass

            try:
                emp3 = request.POST['emp3']
            except:
                pass

            try:
                emp4 = request.POST['emp4']
            except:
                pass

            try:
                emp5 = request.POST['emp5']
            except:
                pass

            try:
                emp6 = request.POST['emp6']
            except:
                pass

            try:
                emp7 = request.POST['emp7']
            except:
                pass

            try:
                emp8 = request.POST['emp8']
            except:
                pass

            try:
                emp9 = request.POST['emp9']
            except:
                pass

            try:
                emp10 = request.POST['emp10']
            except:
                pass

            try:
                emp11 = request.POST['emp11']
            except:
                pass

            try:
                emp12 = request.POST['emp12']
            except:
                pass

            try:
                emp13 = request.POST['emp13']
            except:
                pass

            try:
                emp14 = request.POST['emp14']
            except:
                pass

            try:
                emp15 = request.POST['emp15']
            except:
                pass

            try:
                emp16 = request.POST['emp16']
            except:
                pass

            try:
                emp17 = request.POST['emp17']
            except:
                pass

            try:
                emp18 = request.POST['emp18']
            except:
                pass

            try:
                emp19 = request.POST['emp19']
            except:
                pass

            try:
                emp20 = request.POST['emp20']
            except:
                pass




        
            members = Member.objects.filter(shop=t_shop).last()
            if emp1 == "":
                pass
            else:
                employee1 = UserDetail.objects.filter(user_sharable_id=emp1).last()
                members.user1 = employee1

            if emp2 == "":
                pass
            else:
                employee2 = UserDetail.objects.filter(user_sharable_id=emp2).last()
                members.user2 = employee2

            if emp3 == "":
                pass
            else:
                employee3 = UserDetail.objects.filter(user_sharable_id=emp3).last()
                members.user3 = employee3

            if emp4 == "":
                pass
            else:
                employee4 = UserDetail.objects.filter(user_sharable_id=emp4).last()
                members.user4 = employee4

            if emp5 == "":
                pass
            else:
                employee5 = UserDetail.objects.filter(user_sharable_id=emp5).last()
                members.user5 = employee5

            if emp6 == "":
                pass
            else:
                employee6 = UserDetail.objects.filter(user_sharable_id=emp6).last()
                members.user6 = employee6

            if emp7 == "":
                pass
            else:
                employee7 = UserDetail.objects.filter(user_sharable_id=emp7).last()
                members.user7 = employee7

            if emp8 == "":
                pass
            else:
                employee8 = UserDetail.objects.filter(user_sharable_id=emp8).last()
                members.user8 = employee8

            if emp9 == "":
                pass
            else:
                employee9 = UserDetail.objects.filter(user_sharable_id=emp9).last()
                members.user9 = employee9

            if emp10 == "":
                pass
            else:
                employee10 = UserDetail.objects.filter(user_sharable_id=emp10).last()
                members.user10 = employee10

            if emp11 == "":
                pass
            else:
                employee11 = UserDetail.objects.filter(user_sharable_id=emp11).last()
                members.user11 = employee11

            if emp12 == "":
                pass
            else:
                employee12 = UserDetail.objects.filter(user_sharable_id=emp12).last()
                members.user12 = employee12

            if emp13 == "":
                pass
            else:
                employee13 = UserDetail.objects.filter(user_sharable_id=emp13).last()
                members.user13 = employee13

            if emp14 == "":
                pass
            else:
                employee14 = UserDetail.objects.filter(user_sharable_id=emp14).last()
                members.user14 = employee14

            if emp15 == "":
                pass
            else:
                employee15 = UserDetail.objects.filter(user_sharable_id=emp15).last()
                members.user15 = employee15

            if emp16 == "":
                pass
            else:
                employee16 = UserDetail.objects.filter(user_sharable_id=emp16).last()
                members.user16 = employee16

            if emp17 == "":
                pass
            else:
                employee17 = UserDetail.objects.filter(user_sharable_id=emp17).last()
                members.user17 = employee17

            if emp18 == "":
                pass
            else:
                employee18 = UserDetail.objects.filter(user_sharable_id=emp18).last()
                members.user18 = employee18

            if emp19 == "":
                pass
            else:
                employee19 = UserDetail.objects.filter(user_sharable_id=emp19).last()
                members.user19 = employee19

            if emp20 == "":
                pass
            else:
                employee20 = UserDetail.objects.filter(user_sharable_id=emp20).last()
                members.user20 = employee20

            members.save()
            
            if request.user.is_superuser:
                return HttpResponseRedirect("/Admin/Dashboard")
            else:
                return HttpResponseRedirect("/Admin/user/Dashboard")
    else:
        return HttpResponseRedirect("/login")
    return render(request, "main/shop_builder.html")

def addproduct(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                shop_name = request.POST['shop']
                product_name = request.POST['p_name']
                Price = request.POST['price']
                shops = Shop.objects.filter(user=request.user, pk=shop_name).last()

                if shops.products_added < 30:
                    shops.products_added = shops.products_added+1
                    shops.save()
                    product = Product(shop=shops, Product_Name=product_name, Product_M_R_P=Price)
                    product.save()
                else:
                    shopy = Shop.objects.filter(user=request.user)
                    context = {'shops':shopy, 'refused':True, 'message':"You have already added 30 products in this shop"}
                    return render(request, "main/addproduct.html", context)
                shopy = Shop.objects.filter(user=request.user)
                context = {'shops':shopy, 'success':True}
                return render(request, "main/addproduct.html", context)
            except:
                shopy = Shop.objects.filter(user=request.user)
                context = {'shops':shopy, 'refused':True, 'message':"Fill the form Correctly"}
                return render(request, "main/addproduct.html", context)
        shopy = Shop.objects.filter(user=request.user)
        context = {'shops':shopy}
        return render(request, "main/addproduct.html",context)
    return HttpResponseRedirect("/login")

def addcategory(request):
    if request.user.is_superuser:
        if request.method == "POST":
            cat_name = request.POST['category_name']
            svcat = Category(Name=cat_name)
            svcat.save()
        return HttpResponseRedirect("/Admin/Dashboard")

def adddirectshop(request):
    if request.user.is_superuser:
        if request.method == "POST":
            try:
                shop_name = request.POST['shop']
                shop_latitude = request.POST['latitude']
                shop_longitude = request.POST['longitude']

                store = LocationStore(Name=shop_name, shop_latitude=shop_latitude, shop_longitude=shop_longitude)
                store.save()
                context = {'success':True}
                return render(request, "main/add_directshop.html", context)
            except:
                context = {'refused':True, 'message':"Fill the form Correctly"}
                return render(request, "main/add_directshop.html", context)
        return render(request, "main/add_directshop.html")




