from django.urls import path
from .views import *

urlpatterns = [
    path('top/', index, name='top'),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
    path('list/', listfunc, name='list')
]
