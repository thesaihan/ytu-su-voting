from django.shortcuts import render,redirect
from ajax.common import *
from ajax.models import Vote

def indexFunc(request):
    if classifyAdmin(request,specific=Constant.VALIDATOR):
        return render(request, 'validate/validate.html')
    else:
        return redirect('/login/')
