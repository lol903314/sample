"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from myapp import views
from django.urls import re_path as url

urlpatterns = [
    # path("admin/", admin.site.urls),
    # path("hello/",views.hello)
    url(r"^hello",views.hello),
    url(r"^bmi",views.bmi),
    url(r"^multi",views.multi),
    url(r'^crudops/',views.crudops, name='hello'),
    url(r"^test",views.test),
    url(r"register/",views.register,name='register'),
    url(r"login/",views.login,name='login'),
    url(r"mora/",views.mora,name='mora'),
    url(r"reset/",views.reset,name='reset'),
    url(r"logout/",views.logout,name='logout'),
    url(r"^simpleemail/(?P<emailto>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/",views.sendSimpleEmail,name='sendSimpleEmail'),
]
