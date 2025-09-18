from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from insuranceapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.frontpage, name='frontpage'),
    path('frontpage', views.frontpage, name='frontpage'),
    path('home', views.home, name='home'),
    path('service', views.service, name='service'),
    path('signin', views.signin, name='signin'),
    path('register', views.register, name='register'),
    path('signout', views.signout, name='signout'),
    path('userdata', views.userdata, name='userdata'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),  
]
