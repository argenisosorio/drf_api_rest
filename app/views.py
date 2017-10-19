# -*- coding: utf-8 -*-	
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from app.serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
import requests


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class Index(TemplateView):
    template_name = "index.html"

    def get(self,request,*args, **kwargs):
        """
        En este ejemplo leemos la url que contiene el diccionario con los usuarios
        y usamos el método json.loads
        """
        #data = User.objects.all().order_by('-date_joined')
        url = 'http://192.168.12.180:8000/users/?format=json'
        import urllib, json
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        print data
        return render(request,self.template_name, {'data':data})