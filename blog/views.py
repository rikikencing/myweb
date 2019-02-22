# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse
from .models import Artikel
# Create your views here.

def home (request):
     nama = "R i k i  G u n a w a n"
     keluarga = ['mamah','bapa','ade']
     return render(request,'index.html', {'nama':nama, 'keluarga' :keluarga}) 

def about (request):
    return render(request, 'about.html')

def contact (request):
     return render(request, 'contact.html')

def blog (request):
     # select * from Artikel
     blogs = Artikel.objects.all()
     return render(request, 'blog.html', {'blogs':blogs})
