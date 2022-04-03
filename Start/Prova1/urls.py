from django.urls import path 

from Prova1 import views
urlpatterns = [
    path('',views.index),
    path('rec',views.record),
    path('form1',views.form_name_view),
    path('form2',views.users)
   
]
