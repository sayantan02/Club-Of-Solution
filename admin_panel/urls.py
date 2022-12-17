from django.urls import path
from .import views

urlpatterns = [
    path('Dashboard/',views.Dashboard,name="Dashboard"),
    path('user/Dashboard/',views.userDashboard,name="userDash"),
    path('disapprove/<int:id>/',views.DisApproveShop,name="disapprove"),
    path('approve/<int:id>/',views.ApproveShop,name="approve"),
    path('approveCont/<int:id>/',views.ApproveContact,name="approve_contact"),
    path('approveUserCont/<int:id>/',views.UserViewed,name="approve_user_contact"),
    path('allshops/',views.allshops,name="allshops"),
    path('allproducts/',views.allproducts,name="allproducts"),
    path('AddDetails/',views.AddDetails,name="AddDetails"),
    path('deleteitems/<str:type>/<str:url>/<int:id>/',views.DeleteItems,name="deleteitems"),
    path('createOffer/',views.CreateOffer,name="CreateOffer"),
]