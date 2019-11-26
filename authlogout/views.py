from django.shortcuts import redirect

# Create your views here.
def logoutFunc(request):
    if request.session['admin']:
        del request.session['admin']
    return redirect('/login/')