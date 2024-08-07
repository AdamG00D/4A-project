from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from .views import *



urlpatterns = [
    path('',home,name='home'),
    path('register',register,name='register'),
    path('logout',Logout,name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


