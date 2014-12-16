from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf

def login_user(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if (user is not None):
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/home/')
    context = RequestContext(request)
    context.update(csrf(request))
    return render_to_response('account/login.html', context)


def logout_user(request):
    logout(request)
    return render_to_response('home.html', RequestContext(request))


def home(request):
    return render_to_response('home.html', RequestContext(request))
