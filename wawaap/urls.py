
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery', views.gallery, name='gallery'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('price', views.price, name='price'),
   
    path('business', views.business, name='business'),
    path('commerce', views.commerce, name='commerce'),
    path('art', views.art, name='art'),
    path('webapp', views.webapp, name='webapp'),

]