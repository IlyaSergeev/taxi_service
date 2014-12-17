__author__ = 'hensh'

from django.shortcuts import render_to_response
from TaxiService.required_group_test import group_required
from django.template import RequestContext

def delete(request, ride_id):
    return render_to_response('ride/mock.html', RequestContext(request))

def edit(request, ride_id):
    return render_to_response('ride/mock.html', RequestContext(request))

def create(request):
    return render_to_response('ride/mock.html', RequestContext(request))

def info(request, ride_id):
    return render_to_response('ride/mock.html', RequestContext(request))

def all_for_car(request, car_id):
    return render_to_response('ride/mock.html', RequestContext(request))

