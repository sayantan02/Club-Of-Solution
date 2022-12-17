from django.http.response import HttpResponseRedirect
from main.models import Shop, UserDetail
from django.shortcuts import render
from conference.models import ConferenceRoom
from django.contrib.auth.models import User


def join_chat(request,room_code):
    if request.user.is_authenticated:
        shopRoom = ConferenceRoom.objects.filter(code=room_code).last()
        # detail = UserDetail.objects.filter(user=shopRoom.user).last()
        context = {'room_code':room_code,'shopkeeper':shopRoom.user}
        return render(request, 'conference/join_chat_view.html', context=context)
    else:
        return HttpResponseRedirect("/login")

def prepare_chat_view(request,shop_id):
    if request.user.is_authenticated:
        conference_room = ConferenceRoom.objects.filter(shop=Shop.objects.filter(pk=shop_id).last()).last()
        context = {'room':conference_room}
        return render(request, 'conference/prepare_chat_view.html', context=context)
    else:
        return HttpResponseRedirect("/login")
