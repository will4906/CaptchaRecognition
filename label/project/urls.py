# -*- coding: utf-8 -*-
"""
Created on 2018/3/15

@author: will4906
"""
from django.conf.urls import url

from project import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^image$', views.image, name='image')
]