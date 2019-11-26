from django.shortcuts import redirect
from .models import Admin,Vote
import json

class Constant:
    SUPER_ADMIN = 'Super Admin'
    VOTER = 'Outlet'
    VALIDATOR = 'Validator'

def addVoteCount(candidates):
    res = []
    for c in candidates:
        d = dict()
        d['cand_no'] = c.cand_no
        d['cand_type'] = c.cand_type
        d['cand_id'] = c.cand_type.capitalize() + str(c.cand_no)
        d['name'] = c.name
        d['votecount'] = Vote.objects.filter(**{c.cand_type+'_id':c.cand_no}).count()
        res.append(d)
    return res

def classifyAdmin(request, specific=None):
    adminJson = None

    try:
        adminJson = request.session['admin']
    except KeyError as ke:
        adminJson = None
        
    if adminJson:
        try:
            adminDic = json.loads(adminJson)
            admin = Admin(**adminDic)

            if specific:
                if specific == admin.admintype:
                    return True
                else:
                    return False

            if admin.admintype == Constant.SUPER_ADMIN:
                return redirect('/result/')
            if admin.admintype == Constant.VOTER:
                return redirect('/votenow/')
            if admin.admintype == Constant.VALIDATOR:
                return redirect('/validate/')
        except Exception as e:
            if specific:
                return False
            else:
                return redirect('/login/')

    else:
        if specific:
            return False
        else:
            return redirect('/login/')
