#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'devil fly'
import datetime
from django.contrib.contenttypes.models import ContentType
from read_count.models import ReadNum,ReadDetail
from django.db.models import Sum
from django.utils import timezone

# 每条博客的总访问记录
def each_read(request,obj):
    ct = ContentType.objects.get_for_model(obj)
    key = "%s_%s_read" % (ct.model,obj.pk)
    if not request.COOKIES.get(key):
        #阅读总数加一
        readnum,created = ReadNum.objects.get_or_create(content_type=ct,object_id=obj.pk)
        readnum.reader_num +=1
        readnum.save()
        # 当天阅读总数加一
        date = timezone.now().date()
        readDetail,created = ReadDetail.objects.get_or_create(content_type=ct,object_id=obj.pk,date=date)
        readDetail.reader_num += 1
        readDetail.save()
    return key

# 一周每天的每条博客访问量
def get_week_read_data(content_type):

    today = timezone.now().date()
    dates = []
    read_nums = []
    for i in range(7,0,-1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        read_details = ReadDetail.objects.filter(content_type=content_type,date=date)
        result = read_details.aggregate(read_num_sum=Sum('reader_num'))
        read_nums.append(result['read_num_sum'] or 0)
    return dates,read_nums
# 今日热条
def get_today_hot_data(content_type):
    today = timezone.now().date()
    # 查询出今天的博客按照从大到小排序
    read_details = ReadDetail.objects.filter(content_type=content_type, date=today).order_by('-reader_num')

    return read_details[:7]