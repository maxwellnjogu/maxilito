from django.contrib import admin
from . import views
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings





urlpatterns = [
    path('admin/',views.about ,  name='about'),
    path('', views.home , name='home'),
    path('', views.layout , name='layout')


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


