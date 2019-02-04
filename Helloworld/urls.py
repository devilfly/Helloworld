"""Helloworld URL配置

“urlpatterns”列表将url路由到视图。有关详情，请参阅:

https://docs.djangoproject.com/en/2.1/topics/http/urls/

例子:

功能视图

1. 添加导入:从my_app导入视图

2. 添加一个URL到urlpatterns: path("，视图。家,name = '家')

基于类的观点

1. 添加导入:from other_app。视图导入回家

2. 添加一个URL到urlpatterns: path("， home .as_view()， name='home')

包括另一个URLconf

1. 从django导入include()函数。url导入包括，路径

2. 添加一个URL到urlpatterns: path('blog/'， include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls import static
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
    path('ckeditor',include('ckeditor_uploader.urls')),
    path('blog/',include('blogg.urls')),
    path('comment/', include('comment.urls')),
    path('like/',include('likes.urls')),
    path('user/',include('user.urls')),

]
