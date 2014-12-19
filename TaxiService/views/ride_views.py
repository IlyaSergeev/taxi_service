__author__ = 'hensh'

from django.shortcuts import render_to_response
from TaxiService.required_group_test import group_required
from django.template import RequestContext

def edit(request, ride_id):
    return render_to_response('ride/edit.html', RequestContext(request))

def create(request, car_id):
    return render_to_response('ride/create.html', RequestContext(request))

def all_for_car(request, car_id):
    return render_to_response('ride/rides.html', RequestContext(request))

