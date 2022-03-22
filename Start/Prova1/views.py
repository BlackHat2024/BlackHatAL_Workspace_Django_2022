from cgitb import html
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    a={'insertme':"view.py"}
    return render(request,'Prova1/index.html',context=a)