#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'devil fly'

from django.urls import path
from  . import views

urlpatterns = [
    path('update_comment',views.update_comment,name='update_comment'),

]