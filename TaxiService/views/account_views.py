__author__ = 'hensh'

from TaxiService.required_group_test import group_required
from TaxiService.user_groups import *
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext

def __add_group_if_flag(user, flag, group):
    if flag:
        user.groups.add(group)
    else:
        user.groups.remove(group)

def __fill_user_groups(user, request):
    is_admin = request.POST.get('is_admin', None)
    is_driver = request.POST.get('is_driver', None)
    is_dispatcher = request.POST.get('is_dispatcher', None)

    __add_group_if_flag(user, is_admin, get_group_admin())
    __add_group_if_flag(user, is_driver, get_group_driver())
    __add_group_if_flag(user, is_dispatcher, get_group_dispatcher())

    return user

# TODO redirect to error view
@group_required('Admins')
def account_edit(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Http404
    if request.POST:
        # TODO try password
        password = request.POST['password']
        user.username = request.POST['username']
        user.email = request.POST['email']

        user = __fill_user_groups(user, request)
        user.save()
        return HttpResponseRedirect('/accounts/')
    context = RequestContext(
        request,
        {
            'watching_user' : user,
        },
    )
    return render_to_response('account/edit.html', context)

@group_required('Admins')
def create(request):
    if request.POST:
        new_user = User.objects.create_user(
            request.POST['username'],
            request.POST['email'],
            request.POST['password']
        )
        new_user = __fill_user_groups(new_user, request)
        new_user.save()
        context = RequestContext(
            request,
            {
                'watching_user' : new_user,
            },
        )
        return render_to_response('account/info.html', context)
    return render_to_response('account/create.html', RequestContext(request))

@group_required('Admins')
def account_info(request, user_id):
    watching_user = User.objects.get(id=user_id)
    context = RequestContext(
        request,
        {
            'watching_user' : watching_user,
        },
        )
    return render_to_response('account/info.html', context)

@group_required('Admins')
def accounts(request):
    users = User.objects.all()
    context = RequestContext(
        request,
        {
            'users_list' : users,
        },
        )
    return  render_to_response('account/accounts.html', context)

@group_required('Admins')
def delete(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Http404
    if request.POST:
        # TODO delete tails
        user.delete()
        return HttpResponseRedirect('/accounts/')
    context = RequestContext(
        request,
        {
            'watching_user' : user,
        },
    )
    return render_to_response('account/delete.html', context)