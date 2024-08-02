from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *



urlpatterns = [
    path('',home,name='home'),
    path('login',Login,name='login'),
    path('signup',Signup,name='signup'),
    path('logout',Logout,name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


