from django.urls import path
from . import views

app_name='votenow'

urlpatterns=[
    path('', views.indexFunc, name='index'),
    path('success/', views.successFunc, name='success')
]