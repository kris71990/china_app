"""firstdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from chinaapp import views

prov_regex = "\(2[0-3]|1[0-9]|[1-9]?)/"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^region/(?P<id>(2[0-3]|1[0-9]|[1-9]))/', views.region_detail, name='region_detail'),
    url(r'^region/(?P<id>(2[4-7]))/', views.muni_detail, name='muni_detail'),
    url(r'^region/(?P<id>(2[8-9]|3[0-2]))/', views.aut_reg_detail, name='aut_reg_detail'),
    url(r'^region/(?P<id>(3[3-4]))/', views.adm_reg_detail, name='adm_reg_detail'),
    url(r'^admin/', include(admin.site.urls)),
]
