from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('top/', index, name='top'),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
    path('list/', listfunc, name='list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)