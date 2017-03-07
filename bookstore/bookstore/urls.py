"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import *
from django.contrib import admin
from onlinebookstore import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^admin/doc/',include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search_post/$',views.search,name='search'),
    url(r'^pdf/(?P<pdf_id>[0-9]+)/$', views.open_pdf, name='open_pdf'),
    url(r'^log_in/$',views.log_in,name='log_in'),
    url(r'^log_out/$', views.log_out,name='log_out'),
    url(r'^signup/$',views.signup, name='signup'),
    url(r'aboutus/$',views.aboutus, name='aboutus'),
]
