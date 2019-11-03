from django.urls import path,include
from .views import *
urlpatterns = [
    path('', login, name="login"),
    path('signup', signup, name="signup"),
    path('home', home ,name="home"),
    path('logout', logout, name="logout"),
    ]
