from django.urls import path
from . import views

app_name='authlogout'

urlpatterns = [
    path('', views.logoutFunc, name='logout'),
]
