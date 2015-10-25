"""date URL Configuration

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
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover();

urlpatterns = patterns(
	'',
	url(r'^$', 'main.views.index', name = 'main/index'),
	url(r'^login$', 'login.views.index', name = 'login/index'),
    url(r'^login/submit$', 'login.views.submit', name = 'login/submit'),
    url(r'^register$', 'register.views.index', name = 'register/index'),
    url(r'^admin/', include(admin.site.urls)),
)
