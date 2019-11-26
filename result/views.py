from django.shortcuts import render,redirect
from ajax.common import *
from .models import Candidate

def indexFunc(request):
    if classifyAdmin(request,specific=Constant.SUPER_ADMIN):
        param = {
            'artRes':addVoteCount(Candidate.objects.filter(cand_type='a')),
            'secretaryRes':addVoteCount(Candidate.objects.filter(cand_type='s')),
            'chairmanRes':addVoteCount(Candidate.objects.filter(cand_type='c')),
            }
        print(param)
        return render(request, 'result/result.html', context=param)
    else:
        return redirect('/login/')

