from django.contrib import admin
from django.urls import path
from django.conf.urls import include #添加控制路径的	模块
from rest_framework import routers #路哟配置模块
from ser import views #视图模块
from rest_framework.schemas import get_schema_view #导入辅助函数get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer,OpenAPIRenderer

router = routers.DefaultRouter() #创建路由对象
router.register(r'users',views.UserViewSet)
router.register(r'groups',views.GroupViewSet)

schema_view = get_schema_view(title='ser',renderer_classes=[SwaggerUIRenderer,OpenAPIRenderer])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)), #代表位于根路径
    #api-auth对应授权登录url
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('docs/',schema_view,name='docs')  #配置docs的URL路径
]
