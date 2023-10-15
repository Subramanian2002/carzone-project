from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('About',views.about,name='about'),
    path('cars',views.cars,name='cars'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
]