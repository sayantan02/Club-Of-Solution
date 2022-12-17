from datetime import date, datetime
from main.models import Shop
from main.models import UserDetail
from .models import Transaction
from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import random
from random import randrange

def Payment(request):
    if request.user.is_authenticated:
        if not request.user.is_superuser:
            if UserDetail.objects.filter(user=request.user, payment_initialized=False).last():
                tk_user = User.objects.filter(username=request.user.username).last()
                ud = UserDetail.objects.filter(user=tk_user.id).last()
                if ud.user_sharable_id is None:
                    while True:
                        try:
                            ud.user_sharable_id = RandomIdGen()
                            ud.user_secret = RandomSecretGen()
                            ud.save()
                            break
                        except:
                            pass
                if request.method == "POST":
                    amount = request.POST['amount']
                    user = request.user
                    coll = []

                    for i in User.objects.filter(is_superuser=True):
                        coll.append(i.id)
                    rand = random.choice(coll)
                    collector = User.objects.filter(pk=rand).last()
                    while True:
                        try:
                            transaction = Transaction(retailer=user, collector=collector, balence=int(amount), trans_id=genTransId())
                            transaction.save()
                        
                            ud = UserDetail.objects.filter(user=user).last()
                            ud.payment_initialized = True
                            ud.save()
                            return HttpResponseRedirect("/Admin/user/Dashboard")

                        except:
                            pass
            else:
                if not request.user.is_superuser:
                    return HttpResponseRedirect("/Admin/Dashboard")
                else:
                    return HttpResponseRedirect("/Admin/user/Dashboard")
            date_time = UserDetail.objects.filter(user=request.user).last()
            date = date_time.date_time
            date = date.strftime("%Y-%m-%d %H:%M:%S")
            date = str(date)
            date.split("-")
            date_now = str(datetime.now())
            # print("Dates: ",int(date[0:4])," ", int(date[5:7]), " ",int(date[8:10]), " ",int(date[11:13]), "",int(date[14:16]))
            
            end_date = ""

            if (int(date[11:13])+2) > 23:
                end_time = str(((int(date[11:13])+2)-23)-1)+":"+str(int(date[14:16]))+":00"
                end_date = ""
                if (int(date[5:7])) == 1:
                    end_date = f"Jan {str(int(date[8:10])+1)},{str(int(date[0:4]))} "
                elif int(date[5:7]) == 2:
                    end_date = f"Feb {str(int(date[8:10])+1)},{str(int(date[0:4]))} "
                elif int(date[5:7]) == 3:
                    end_date = f"Mar {str(int(date[8:10])+1)},{str(int(date[0:4]))} "
                elif int(date[5:7]) == 4:
                    end_date = f"Apr {str(int(date[8:10])+1)},{str(int(date[0:4]))} "
                elif int(date[5:7]) == 5:
                    end_date = f"May {str(int(date[8:10])+1)},{str(int(date[0:4]))} "
                elif int(date[5:7]) == 6:
                    end_date = f"Jun {str(int(date[8:10])+1)},{str(int(date[0:4]))} "
                elif int(date[5:7]) == 7:
                    end_date = f"Jul {str(int(date[8:10])+1)},{str(int(date[0:4]))} "
                elif int(date[5:7]) == 8:
                    end_date = f"Aug {str(int(date[8:10])+1)},{str(int(date[0:4]))} "
                elif int(date[5:7]) == 9:
                    end_date = f"Sep {str(int(date[8:10])+1)},{str(int(date[0:4]))} "
                elif int(date[5:7]) == 10:
                    end_date = f"Oct {str(int(date[8:10])+1)},{str(int(date[0:4]))} "
                elif int(date[5:7]) == 11:
                    end_date = f"Nov {str(int(date[8:10])+1)},{str(int(date[0:4]))} "
                elif int(date[5:7]) == 12:
                    end_date = f"Dec {str(int(date[8:10])+1)},{str(int(date[0:4]))} "
            else:
                end_time = str(int(date[11:13])+2)+":"+str(int(date[14:16]))+":00"

                if int(date[5:7]) == 1:
                    end_date = f"Jan {str(int(date[8:10]))},{str(int(date[0:4]))} "
                elif int(date[5:7]) == 2:
                    end_date = f"Feb {str(int(date[8:10]))},{str(int(date[0:4]))} "
                elif int(date[5:7]) == 3:
                    end_date = f"Mar {str(int(date[8:10]))},{str(int(date[0:4]))} "
                elif int(date[5:7]) == 4:
                    end_date = f"Apr {str(int(date[8:10]))},{str(int(date[0:4]))} "
                elif int(date[5:7]) == 5:
                    end_date = f"May {str(int(date[8:10]))},{str(int(date[0:4]))} "
                elif int(date[5:7]) == 6:
                    end_date = f"Jun {str(int(date[8:10]))},{str(int(date[0:4]))} "
                elif int(date[5:7]) == 7:
                    end_date = f"Jul {str(int(date[8:10]))},{str(int(date[0:4]))} "
                elif int(date[5:7]) == 8:
                    end_date = f"Aug {str(int(date[8:10]))},{str(int(date[0:4]))} "
                elif int(date[5:7]) == 9:
                    end_date = f"Sep {str(int(date[8:10]))},{str(int(date[0:4]))} "
                elif int(date[5:7]) == 10:
                    end_date = f"Oct {str(int(date[8:10]))},{str(int(date[0:4]))} "
                elif int(date[5:7]) == 11:
                    end_date = f"Nov {str(int(date[8:10]))},{str(int(date[0:4]))} "
                elif int(date[5:7]) == 12:
                    end_date = f"Dec {str(int(date[8:10]))},{str(int(date[0:4]))} "

            date_now.split("-")

            status = False
            # print("Dates: ",date_now[0:4]," ", date_now[5:7], " ",date_now[8:10], " ",date_now[11:13], "",date_now[14:16])
            if int(date_now[8:10]) >= int(date[8:10]):
                if int(date_now[5:7]) >= int(date[5:7]):
                    if int(date_now[0:4]) >= int(date[0:4]):

                        if (int(date[11:13])+2) > int(date_now[11:13]):
                            status = True
                        elif (int(date[11:13])+2) == int(date_now[11:13]):
                            if (int(date[14:16])) > int(date_now[14:16]):
                                status = True
                            else:
                                status = False
                        else:
                            status = False
                    else:
                        status = False
                else:
                    status = False
            else:
                status = False

            end_date_time = end_date+end_time
            print(end_date_time)
            print(status)
            context = {'ending':end_date_time, 'offer_status':status}
            return render(request, "payment_manager/pricing.html", context)
        else:
            return HttpResponseRedirect("/Admin/Dashboard")
    else:
        return HttpResponseRedirect("/login")

def RandomIdGen():
     return str(randrange(1, 99999999))

def RandomSecretGen():
     return str(randrange(1, 999999999999))

def genTransId():
    return str(randrange(1, 99999999999999))

def PaymentDone(request):
    if request.user.is_superuser:
        if request.method == "POST":
            user_id = request.POST['user_id']
            # shop_name = request.POST['shop']
            admin_secret = request.POST['secret']

            t_retailer = UserDetail.objects.filter(user_sharable_id=user_id).last()
            t_collector = UserDetail.objects.filter(user_secret=admin_secret).last()
            # shop = Shop.objects.filter(Name=shop_name).last()
            transaction = Transaction.objects.filter(retailer=t_retailer.user, collector=t_collector.user).last()
            transaction.transaction_completed = True
            transaction.save()
            t_retailer.payment_succeed = True
            t_retailer.save()
            return HttpResponseRedirect("/Admin/Dashboard")
        else:
            print("else")
            return HttpResponseRedirect("/Admin/Dashboard")




