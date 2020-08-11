from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from API.serializers import UserSerializer,GroupSerializer


# Create your views here.

#viewsets通过serializer_class找到对应的serializers
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all() #将User的所有对象都赋给queryset，并返回对应值
	serializer_class = UserSerializer #指向UserSerilizer（返回定义的字段）

class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer