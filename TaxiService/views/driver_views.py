__author__ = 'hensh'

from django.shortcuts import render_to_response
from django.template import RequestContext
from TaxiService.models import Driver, User
from TaxiService.required_group_test import group_required
from TaxiService.user_groups import get_group_driver

class Driver_info:
    def __init__(self, user = None, driver = None):
        self.user = user
        self.driver = driver


def find_by_user(drivers, user):
    return next((driver for driver in drivers if driver.account.id == user.id), None)

@group_required('Admins')
def drivers(request):
    drivers = Driver.objects.all()
    users = get_group_driver().user_set.all()
    result = []
    for user in users:
        result.append(Driver_info(
            user = user,
            driver = find_by_user(drivers, user)
        ))
    context = RequestContext(
        request,
        {
            'drivers' : result
        }
    )
    return render_to_response('driver/drivers.html', context)

@group_required('Admins')
def edit(request, driver_id):
    return render_to_response('driver/edit.html', RequestContext(request))