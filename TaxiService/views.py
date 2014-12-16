from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from TaxiService.models import *
from TaxiService.user_groups import *
from TaxiService.permissions import *
from TaxiService.required_group_test import group_required

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

# TODO redirect to error view
@group_required('Admins')
def signup(request):
    if request.POST:
        password = request.POST['password']
        username = request.POST['username']
        email = request.POST['email']
        is_admin = request.POST.get('is_admin', None)
        is_driver = request.POST.get('is_driver', None)
        is_dispatcher = request.POST.get('is_dispatcher', None)
        new_user = User.objects.create_user(username, email, password)
        if is_admin:
            new_user.groups.add(get_group_admin())
        if is_driver:
            new_user.groups.add(get_group_driver())
        if is_dispatcher:
            new_user.groups.add(get_group_dispatcher())
        new_user.save()
        return HttpResponseRedirect('/home/')
    return render_to_response('account/signup.html', RequestContext(request))
