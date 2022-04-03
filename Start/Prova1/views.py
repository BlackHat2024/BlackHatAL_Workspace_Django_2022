from cgitb import html
import email
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from Prova1.models import AccessRecord,Webpage,Topic
from Prova1.forms import FormName,NewUserForm
from . import forms
# Create your views here.

def index(request):
    return render(request,'Prova1/index.html')

def record(request):
    webpage_list = AccessRecord.objects.order_by('date')
    dd = {'ar':webpage_list}
    return render(request,'Prova1/a.html',context=dd)

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])

    return render(request,'Prova1/form1.html',{'form':form})

def users(request):

    form2 = NewUserForm()

    if request.method == "POST":
        form2 = NewUserForm(request.POST)

        if form2.is_valid():
            form2.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'Prova1/form2.html',{'form2':form2})