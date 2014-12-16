__author__ = 'hensh'

from TaxiService.required_group_test import group_required
from TaxiService.user_groups import *
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

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
