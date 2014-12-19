__author__ = 'hensh'

from django.shortcuts import render_to_response
from TaxiService.required_group_test import group_required
from django.template import RequestContext
from TaxiService.models import Car
from django.http import HttpResponseRedirect, Http404
from datetime import datetime

def edit(request, ride_id):
    return render_to_response('ride/edit.html', RequestContext(request))

def create(request, car_id):
    context = RequestContext(
        request,
        {
            'datetime' : datetime.now(),
            'car_id' : car_id
        },
    )
    return render_to_response('ride/create.html', context)

def all_for_car(request, car_id):
    try:
        car = Car.objects.get(id = car_id)
    except Car.DoesNotExist:
        return Http404

    context = RequestContext(
        request,
        {
            'car' : car,
        }
    )
    return render_to_response('ride/rides.html', context)

