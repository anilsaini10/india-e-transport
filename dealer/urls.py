from django.urls.resolvers import URLPattern
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('driver-form', views.driver, name="driver-form"),
    path('dealer-form', views.dealer, name="dealer-form"),
    path('login', views.signin, name="login"),
    path('logout', views.signout, name="logout"),
]
