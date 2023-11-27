from django.contrib import admin
from django.urls import path, re_path
from . import views
from Portafolio.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', home, name='home'),
    path('home/', home, name='home'),
]
