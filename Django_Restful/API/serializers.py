#/usr/bin/env python
#-*- coding:utf-8 -*-

#导入系统自带的两个表格
from django.contrib.auth.models import User,Group
#导入serializers模块
from rest_framework import serializers

#创建User序列化类，继承内置方法；定义users表的相关字段
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User  #指向前端的users表
		fields = ('url','username','email','group') #配置Users表字段

#创建group序列化类；定义group表的相关字段
class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group  #指向前端的group表
		fields = ('url','name') #配置group表字段,url和users表中URL一致