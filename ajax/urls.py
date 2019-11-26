from django.urls import path
from . import views

app_name='ajaxUrl'

urlpatterns=[
    path('checkAdmin/', views.checkAdminFunc, name='checkAdmin'),
    path('checkValidate/', views.checkValidateFunc, name='checkValidate'),
    path('checkVote/', views.checkVoteFunc, name='checkVote'),
]