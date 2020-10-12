from django.urls import path, include
from . import views


urlpatterns = [
    path('index', views.index, name='intro page'),
    path('home', views.home, name='invitation'),
    path('contact', views.contact, name='contact'),
]
