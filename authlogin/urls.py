from django.urls import include,path
from . import views,apps

app_name=apps.AuthloginConfig.name

urlpatterns=[
    path('', views.indexFunc, name='index'),
    path('login/', views.indexFunc, name='login'),
]