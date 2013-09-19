#coding=utf-8
from django.conf.urls import patterns, url

import views

urlpatterns = patterns(
    url(r'^$', views.index, name='index'), 
    url(r'filetopic$', views.filetopic, name='filetopic'), 
    url(r'getpic$', views.getPic, name='getpic')
)
