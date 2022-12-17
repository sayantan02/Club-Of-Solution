from payment_manager.models import Transaction
from main.models import OfferTimeline, Product
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from main.models import Shop,Contact, UserDetail
from django.contrib.auth.models import User

# Create your views here.
def Dashboard(request):
    if request.user.is_superuser:
        users = User.objects.all()
        shop = Shop.objects.all()
        userdetails = UserDetail.objects.filter(user=request.user).last()
        ApprovedShops = Shop.objects.filter(Approved=True,Cancelled=False)
        unApprovedShops = Shop.objects.filter(Approved=False,Cancelled=False)
        incomplete_transactions = Transaction.objects.all()
        offers = OfferTimeline.objects.all()
        contact = Contact.objects.filter(viewed=False)
        context = {'shop':shop,'Approved_shops':ApprovedShops,'users':len(users),'unapproved_shops':unApprovedShops, 'contacts':contact, 'userdetail':userdetails, 'incomplete_transactions':incomplete_transactions,'offers':offers}

        return render(request,"admin_panel/dashboard.html",context)
    else:
        return HttpResponseRedirect("/Admin/user/Dashboard")

def ApproveContact(request,id):
    cont = Contact.objects.filter(pk=id).first()
    cont.viewed = True
    cont.save()
    return HttpResponseRedirect("/Admin/Dashboard")

def ApproveShop(request,id):
    shop = Shop.objects.filter(pk=id).first()
    shop.Approved = True
    shop.save()
    return HttpResponseRedirect("/Admin/Dashboard")

def DisApproveShop(request,id):
    shop = Shop.objects.filter(pk=id).first()
    shop.Cancelled = True
    shop.save()
    return HttpResponseRedirect("/Admin/Dashboard")

def userDashboard(request):
    if request.user.is_authenticated:
        if not request.user.is_superuser:
            ud = UserDetail.objects.filter(user=request.user).last()
            if ud.payment_initialized:
                shop = Shop.objects.filter(user=request.user)
                ApprovedShops = Shop.objects.filter(user=request.user,Approved=True,Cancelled=False)
                unApprovedShops = Shop.objects.filter(user=request.user,Approved=False,Cancelled=False)
                cancelledShops = Shop.objects.filter(user=request.user,Approved=False,Cancelled=True)
                contacts = Contact.objects.filter(Username=request.user.username, user_viewed=False)
                userdetails = UserDetail.objects.filter(user=request.user).last()
                transaction = Transaction.objects.filter(retailer=request.user).last()
                collector = UserDetail.objects.filter(user=transaction.collector).last()
                offers = OfferTimeline.objects.filter(shop=shop)
                all_products = []
                for i in Shop.objects.filter(user=request.user):
                    for i in Product.objects.filter(shop=i):
                        all_products.append(i)

                context = {'shop':shop,'Approved_shops':ApprovedShops, 'userdetail':userdetails, 'products':all_products, 'unapproved_shops':unApprovedShops, 'cancelled_shops':cancelledShops,'collector':collector, 'transaction':transaction, 'contacts':contacts,'offers':offers}
                return render(request,"admin_panel/user_dashboard.html",context)
            else:
                return HttpResponseRedirect("/payment_manager/payment")
        else:
            return HttpResponseRedirect("/Admin/Dashboard")
    else:
        return HttpResponseRedirect("/login")

def allshops(request):
    if request.user.is_authenticated:
        if not request.user.is_superuser:
            ApprovedShops = Shop.objects.filter(user=request.user,Approved=True,Cancelled=False)
            unApprovedShops = Shop.objects.filter(user=request.user,Approved=False,Cancelled=False)
            cancelledShops = Shop.objects.filter(user=request.user,Approved=False,Cancelled=True)
            userdetails = UserDetail.objects.filter(user=request.user).last()
            shop = Shop.objects.filter(user=request.user)
            context = {'Approved_shops':ApprovedShops, 'userdetail':userdetails, 'unapproved_shops':unApprovedShops, 'cancelled_shops':cancelledShops,'shop':shop}
            return render(request, "admin_panel/all_shops.html", context)
        elif request.user.is_superuser:
            users = User.objects.all()
            userdetails = UserDetail.objects.filter(user=request.user).last()
            ApprovedShops = Shop.objects.filter(Approved=True,Cancelled=False)
            unApprovedShops = Shop.objects.filter(Approved=False,Cancelled=False)
            contact = Contact.objects.filter(viewed=False)
            shops = Shop.objects.all()
            context = {'shop':shops,'Approved_shops':ApprovedShops,'users':len(users),'unapproved_shops':unApprovedShops, 'contacts':contact, 'userdetail':userdetails}
            return render(request, "admin_panel/all_shops.html", context)
    else:
        return HttpResponseRedirect("/login")

def allOffers(request):
    if request.user.is_authenticated:
        if not request.user.is_superuser:
            shops = Shop.objects.filter(user=request.user)
            Offers = []
            for i in shops:
                Offers.append(OfferTimeline.objects.filter(shop=i).last())
            context = {'offers':Offers}
            return render(request, "admin_panel/all_shops.html", context)
        
        elif request.user.is_superuser:
            Offers = OfferTimeline.objects.all()
            context = {'offers':Offers}
            return render(request, "admin_panel/all_shops.html", context)
    else:
        return HttpResponseRedirect("/login")

def allproducts(request):
    if request.user.is_authenticated:
        if not request.user.is_superuser:
            ApprovedShops = Shop.objects.filter(user=request.user,Approved=True,Cancelled=False)
            unApprovedShops = Shop.objects.filter(user=request.user,Approved=False,Cancelled=False)
            cancelledShops = Shop.objects.filter(user=request.user,Approved=False,Cancelled=True)
            userdetails = UserDetail.objects.filter(user=request.user).last()
            all_products = []
            for i in Shop.objects.filter(user=request.user):
                for i in Product.objects.filter(shop=i):
                    all_products.append(i)
            context = {'Approved_shops':ApprovedShops, 'userdetail':userdetails, 'unapproved_shops':unApprovedShops, 'cancelled_shops':cancelledShops,'products':all_products}
            return render(request, "admin_panel/all_products.html", context)
        elif request.user.is_superuser:
            users = User.objects.all()
            userdetails = UserDetail.objects.filter(user=request.user).last()
            ApprovedShops = Shop.objects.filter(Approved=True,Cancelled=False)
            unApprovedShops = Shop.objects.filter(Approved=False,Cancelled=False)
            contact = Contact.objects.filter(viewed=False)
            product = Product.objects.all()
            context = {'products':product,'Approved_shops':ApprovedShops,'users':len(users),'unapproved_shops':unApprovedShops, 'contacts':contact, 'userdetail':userdetails}
            return render(request, "admin_panel/all_products.html", context)
    else:
        return HttpResponseRedirect("/login")

def DeleteItems(request,type,url,id):
    if request.user.is_authenticated:
        if not request.user.is_superuser:
            if type == "product":
                for i in Shop.objects.filter(user=request.user):
                    Product.objects.filter(pk=id, shop=i).delete()
            elif type == "shop":
                Shop.objects.filter(user=request.user, pk=id).delete()
        elif request.user.is_superuser:
            if type == "product":
                Product.objects.filter(pk=id).delete()
            elif type == "shop":
                Shop.objects.filter(pk=id).delete()

    
    e_url = url.replace("+","/")
    return HttpResponseRedirect("/"+e_url)

def AddDetails(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            City = request.POST['city']
            Phone = request.POST['phone_number']
            userdetails = UserDetail.objects.filter(user=request.user).last()
            userdetails.city = City
            userdetails.phone_number = Phone
            userdetails.save()
    return HttpResponseRedirect("/Admin/user/Dashboard")

def UserViewed(request,id):
    cont = Contact.objects.filter(pk=id).first()
    cont.user_viewed = True
    cont.save()
    return HttpResponseRedirect("/Admin/Dashboard")

def CreateOffer(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            if not request.user.is_superuser:

                offer_Name = request.POST['offer_name']
                shop = Shop.objects.filter(request.POST['shop_id'])
                product = request.POST['product_id']
                text = request.POST['text']
                current_Price = request.POST['current_price']
                Image = request.FILES['image']
                Ending_date = request.POST['ending']
                product_name = request.POST['product_name']

                create_offer = OfferTimeline(
                                Offer_Name=offer_Name,
                                shop = shop,
                                Product_Offer = Product.objects.filter(pk=int(product)).last(), 
                                Product_Name = product_name, 
                                text = text, 
                                current_price = current_Price, 
                                picture = Image, 
                                Ending_Date = Ending_date
                              )
                create_offer.save()
                return HttpResponseRedirect("/Admin/user/Dashboard")
            else:
                return HttpResponseRedirect("Admin/Dashboard")
        return HttpResponseRedirect("/login")
    return HttpResponse("This Url Is not for the Request you Sent to It.")



