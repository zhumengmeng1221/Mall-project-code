"""MmShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
import xadmin
from rest_framework.authtoken import views

#配置媒体文件路径
from MmShop.settings import MEDIA_ROOT
from django.views.static import serve
# from goods.views_base import GoodsListView

from rest_framework.documentation import include_docs_urls
from goods.views import GoodsListViewSet,CategoryViewset
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from users.views import SmsCodeViewset,UserViewset
router = DefaultRouter()

# 配置goods的url
router.register(r'goods', GoodsListViewSet,base_name="goods")
# 配置category的url
router.register(r'categorys', CategoryViewset, base_name="categorys")

# 配置code的url
router.register(r'codes', SmsCodeViewset, base_name="codes")

# 配置users的url
router.register(r'users', UserViewset, base_name="users")

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r"^media/(?P<path>.*)$",serve,{"document_root":MEDIA_ROOT}),

    # 商品列表

    url('', include(router.urls)),
    # 生成drf自动文档配置
    url(r"^docs/",include_docs_urls(title="慕学生鲜")),

    url(r'^api-auth/', include('rest_framework.urls')),
    # drf自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),
    # jwt的认证接口
    url(r'^login/', obtain_jwt_token),

]

