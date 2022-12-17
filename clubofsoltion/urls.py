from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('accounts/', include('allauth.urls')),
    path('Admin/',include("admin_panel.urls")),
    path('location_manager/',include("location_manager.urls")),
    path('payment_manager/',include("payment_manager.urls")),
    path('conference/',include("conference.urls")),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
