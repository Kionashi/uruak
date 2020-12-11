"""Routes"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import landing as landing_views

urlpatterns = [
    path('', landing_views.home, name='home'),
    path('about', landing_views.about, name='about'),
    path('contact', landing_views.contact, name='contact'),
    path('products', landing_views.products, name='products'),
]