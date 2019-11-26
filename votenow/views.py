from django.shortcuts import render,redirect
from ajax.common import *
from ajax.models import Vote

def successFunc(request):
    if classifyAdmin(request,specific=Constant.VOTER):
        return render(request, 'votenow/success.html')
    else:
        return redirect('/login/')

def indexFuncGET(request):
    if classifyAdmin(request,specific=Constant.VOTER):
        return render(request, 'votenow/votenow.html')
    else:
        return redirect('/login/')


def indexFuncPOST(request):
    if classifyAdmin(request,specific=Constant.VOTER):
        votes = Vote.objects.filter(pk=request.POST['entrance_id'])
        v = votes[0]
        v.c_id = request.POST['selectedChairman']
        v.s_id = request.POST['selectedSecretary']
        v.a_id = request.POST['selectedArt']
        v.save()
        return redirect('success/')
    else:
        return redirect('/login/')


def indexFunc(request):
    if request.method == 'GET':
        return indexFuncGET(request)
    if request.method == 'POST':
        return indexFuncPOST(request)