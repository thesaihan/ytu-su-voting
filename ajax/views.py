from django.shortcuts import render
from ajax.models import Admin,Vote
from django.http import JsonResponse

def checkAdminFunc(request):
    r = str(request.get_full_path())
    username = r[r.index('?')+1:r.index('%')]
    password = r[r.index('%7C')+3:]
    aqs = Admin.objects.filter(username=username,password=password)
    if aqs:
        a = aqs[0]
        adic = {}
        adic['username']=a.username
        adic['password']=a.password
        adic['adminType']=a.admintype
        return JsonResponse(adic)
    else:
        return JsonResponse('',safe=False)

def checkValidateFunc(request):
    r = str(request.get_full_path())
    eid = r[r.index('?')+1:]
    aqs = Vote.objects.filter(entrance_id=eid)
    adic = {}
    if aqs:
        adic['validated'] = True
    else:
        v = Vote(entrance_id=eid)
        v.save()
        adic['validated'] = False
    return JsonResponse(adic,safe=False)

def checkVoteFunc(request):
    r = str(request.get_full_path())
    eid = r[r.index('?')+1:]
    votes = Vote.objects.filter(entrance_id=eid)
    votedic = {}
    if votes:
        votedic['isValidated'] = True
        vote = votes[0]
        if vote.c_id and vote.s_id and vote.a_id :
            votedic['isVoted'] = True
        else:
            votedic['isVoted'] = False
    else:
        votedic['isValidated'] = False
        votedic['isVoted'] = False

    return JsonResponse(votedic,safe=False)