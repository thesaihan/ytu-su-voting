from django.shortcuts import render,redirect
from ajax.models import Admin
from ajax.common import *

# Create your views here.

def indexFunc(request):
    if request.method == 'GET':
        return render(request,'authlogin/index.html')

    if request.method == 'POST':
        #print('login/ post method')
        username = request.POST['username']
        password = request.POST['password']
        #print(username,password)
        aqs = Admin.objects.filter(username=username, password = password)
        #print(aqs)
        if aqs:
            admin = aqs[0]
            request.session['admin']=admin.__str__()
            return classifyAdmin(request)
        else:
            return redirect('/login/')