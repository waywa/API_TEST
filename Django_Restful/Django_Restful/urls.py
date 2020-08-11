from django.contrib import admin
from django.urls import path
from django.conf.urls import include #控制添加路径的模块
from rest_framework import routers #路由配置模块
from API import views

#导入辅助函数
# from rest_framework.schemas import get_schema_view
# #导入两个类
# from rest_framework_swagger.renderers import SwaggerUIRenderer,OpenAPIRenderer

router = routers.DefaultRouter()  #创建路由对象
router.register(r'users',views.UserViewSet) #调用register方法，配置Users的路由
router.register(r'group',views.GroupViewSet) #配置group路由

#利用辅助函数引入所导入的两个类
#schema_view = get_schema_view(title='API',renderer_classes=[SwaggerUIRenderer,OpenAPIRenderer])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)), #代表位于根路径的主域名127.0.0.1:8000
    #api-auth对应授权登录URL
    path('api-auth/',include('rest_framework.urls',namespace = 'rest_framework'))
    #path('docs/',schema_view,name='docs')
]
