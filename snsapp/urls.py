from django.urls import path
from .views import *

urlpatterns = [
    path('top/', index),
    path('signup/', signupfunc),
    path('login/', loginfunc),
]
