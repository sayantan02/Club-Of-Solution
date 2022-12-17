from django.urls import path
from .import views

urlpatterns = [
    path('payment/',views.Payment,name="payment"),
    path('apply_payment_succeed/',views.PaymentDone,name="payment-done"),
]