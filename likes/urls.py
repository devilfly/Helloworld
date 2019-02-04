#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'devil fly'

from django.urls import path
from  . import views

urlpatterns = [
    path('like_change',views.like_change,name='like_change'),

]