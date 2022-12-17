from django.urls import path
from . import views

# app_name='rooms'

urlpatterns = [
    path('pre_conference/<int:shop_id>/', views.prepare_chat_view, name='prepare_chat_view'),
    path('join_chat_view/<str:room_code>/', views.join_chat, name='join_chat'),
]