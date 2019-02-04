from django.shortcuts import render,get_object_or_404
from .models import Blog,BlogType
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Count
from read_count.utils import each_read

# 分页处理 供其他方法使用
def get_common_blog_list_data(request,blog_all_list):
    paginator = Paginator(blog_all_list, settings.EACH_PAGE_BLOG_COUNT)  # 每页数量
    page_num = request.GET.get('page', 1)  # 获取Url的页面参数
    each_page_blogs = paginator.get_page(page_num)
    currentr_page_num = each_page_blogs.number
    # 页码前后两页
    page_range = list(range(max(currentr_page_num - 2, 1), currentr_page_num)) + \
                 list(range(currentr_page_num, min(currentr_page_num + 2, paginator.num_pages) + 1))
    # 加上省略号标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    context = {}
    blog_date_dict = {}
    blog_dates = Blog.objects.dates('created_time', 'month', order='DESC')  # 时间降序列出日期归档
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(created_time__year=blog_date.year,
                                         created_time__month=blog_date.month).count()
        blog_date_dict[blog_date] = blog_count
    context['blogs'] = each_page_blogs.object_list #公共的每页博客列表
    context['each_page_blogs'] = each_page_blogs #每页博客判断有无下一条
    context['page_range'] = page_range #博客共有几页
    context['blog_types'] = BlogType.objects.annotate(blog_count=Count('blog') ) #博客类型 对服务器损耗小
    context['blog_date_dict'] = blog_date_dict  # 博客共有几页
    return context
# 博客列表展示
def blog_list(request):
    blog_all_list = Blog.objects.all()
    context = get_common_blog_list_data(request,blog_all_list)
    return render(request,'blog/blog_list.html', context)
# 按博客分类
def blog_with_type(request,blog_type_pk):

    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    blog_all_list = Blog.objects.filter(blog_type=blog_type)
    context = get_common_blog_list_data(request,blog_all_list)
    context['blog_type'] = blog_type
    return render(request,'blog/blog_with_type.html', context)
# 按博客发布时间分类
def blog_with_date(request,year,month):
    blog_all_list = Blog.objects.filter(created_time__year=year,created_time__month=month)
    context = get_common_blog_list_data(request,blog_all_list)
    context['blogs_with_dates'] = '%s年%s月' % (year,month)
    return render(request,'blog/blog_with_date.html', context)
# 每条博客详情
def blog_detail(request,blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    # 判断是否浏览过
    read_key = each_read(request,blog)
    context = {}
    # 获取该条博客信息
    context['blog'] = blog
    # 根据时间获取上一页
    context['previous_blog'] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    # 下一页
    context['next_blog'] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    response = render(request,'blog/blog_detail.html', context)
    response.set_cookie(read_key ,'true')
    return response