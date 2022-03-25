from cgitb import html
from django.shortcuts import render
from django.http import HttpResponse
from Prova1.models import AccessRecord,Webpage,Topic

# Create your views here.

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    dd = {'ar':webpage_list}
    return render(request,'Prova1/index.html',context=dd)