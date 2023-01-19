from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns =[

    path('',views.inicio,name= 'inicio'),
    path('login/',views.ingreso,name= 'ingreso'),
    path('registro/',views.registro,name='registro'),
    path('sobremi/',views.sobremi,name='sobremi'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('editarperfil/',views.editarperfil,name= 'editarperfil'),
    path('posteo/',views.posteo,name= 'post'),
]