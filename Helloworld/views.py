#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'devil fly'
import datetime
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.db.models import Sum
from django.utils import timezone
from django.core.cache import cache
from read_count.utils import get_week_read_data,get_today_hot_data
from blogg.models import Blog


# 获取七天热点博客
def get_week_hot_data():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)

    # 查询出七天的博客按照从大到小排序
    blogs = Blog.objects.filter(readDetails__date__lt=today,readDetails__date__gte=date)\
                        .values('id','title')\
                        .annotate(read_num_sum=Sum('readDetails__reader_num'))\
                        .order_by('-read_num_sum')
    return blogs[:7]

# 访问入口
def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates,read_nums = get_week_read_data(blog_content_type)
    # 获取七天缓存数据
    get_week_hot_blog = cache.get('get_week_hot_blog')
    if get_week_hot_blog is None:
        get_week_hot_blog = get_week_hot_data()
        cache.set('get_week_hot_blog',get_week_hot_blog,3600)

    context = {}
    context['dates'] = dates
    context['read_nums'] = read_nums
    context['today_hot_datas'] = get_today_hot_data(blog_content_type)
    context['get_week_hot_data'] = get_week_hot_blog
    return render(request,'home.html',context)

