""" URL Configuration
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
from django.conf.urls import include, url
from django.contrib import admin
from user import urls as user_urls

from nutr.urls import nutdata as nutdata_urls, nutrdef as nutrdef_urls, epacolo as epacolo_urls

urlpatterns = [
    url(r'^epacolo/', include(epacolo_urls)),
    url(r'^nutrdef/', include(nutrdef_urls)),
    url(r'^nutdata/', include(nutdata_urls)),
    url(r'^user/',
        include(
            user_urls,
            app_name='user',
            namespace='dj-auth')),
]
