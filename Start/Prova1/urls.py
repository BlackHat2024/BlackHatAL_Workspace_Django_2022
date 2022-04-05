from django.urls import path 

from Prova1 import views
urlpatterns = [
    path('',views.index,name='index'),
    path('rec',views.record),
    path('form1',views.form_name_view),
    path('form2',views.users),
    path('home',views.lrhome,name='lrhome'),
    path('userpage',views.userpage,name='userpage'),
    path('reg',views.register,name='register'),
    path('logout', views.user_logout, name='logout'),
    path('log',views.user_login,name='user_login')
   
]
