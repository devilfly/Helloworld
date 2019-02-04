#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'devil fly'

from .forms import LoginForm


def login_modal_form(request):
    return {'login_modal_form': LoginForm()}