__author__ = 'hensh'

from django.shortcuts import render_to_response
from TaxiService.required_group_test import group_required
from django.template import RequestContext
from TaxiService.models import Car

# TODO delete this
def mock1(request):
    return render_to_response('car/mock.html', RequestContext(request))

# TODO delete this
def mock(request, user_id):
    return render_to_response('car/mock.html', RequestContext(request))

def cars(request):
    context = RequestContext(
        request,
        {
            'cars_list' : Car.objects.all(),
        }
    )
    return render_to_response('car/cars.html', context)