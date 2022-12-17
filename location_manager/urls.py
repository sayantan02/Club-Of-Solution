from django.urls import path
from .import views

urlpatterns = [
    path('getlatlon/',views.getLatLon,name="getlatlon"),
    path('savelatlon/<str:name>/',views.saveLatLon,name="savelatlon"),
]