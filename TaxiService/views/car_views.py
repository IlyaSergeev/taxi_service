__author__ = 'hensh'

from django.shortcuts import render_to_response
from TaxiService.required_group_test import group_required
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404
from TaxiService.models import Car

# TODO delete this
def mock1(request):
    return render_to_response('car/mock.html', RequestContext(request))

# TODO delete this
def mock(request, user_id):
    return render_to_response('car/mock.html', RequestContext(request))

@group_required('Admins', 'Dispatchers')
def cars(request):
    context = RequestContext(
        request,
        {
            'cars_list' : Car.objects.all(),
        }
    )
    return render_to_response('car/cars.html', context)

def create(request):
    if request.POST:
        # TODO make validation
        car = Car()
        car.brand = request.POST['brand']
        car.model = request.POST['model']
        car.color = request.POST['color']
        car.reg_number = request.POST['reg_number']
        car.save()
        return HttpResponseRedirect('/cars/')
    return render_to_response('car/create.html', RequestContext(request))

def edit(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        return Http404
    if request.POST:
        car.brand = request.POST['brand']
        car.model = request.POST['model']
        car.color = request.POST['color']
        car.reg_number = request.POST['reg_number']
        # TODO make validation
        car.save()
        return HttpResponseRedirect('/cars/')
    context = RequestContext(
        request,
        {
            'watching_car' : car,
        },
    )
    return render_to_response('car/edit.html', context)

def delete(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        return Http404
    if request.POST:
        # TODO refresh driver info
        car.delete()
        return HttpResponseRedirect('/cars/')
    context = RequestContext(
        request,
        {
            'car' : car,
        },
    )
    return render_to_response('car/delete.html', context)

def info(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        return Http404
    context = RequestContext(
    request,
        {
            'car' : car,
        },
    )
    return render_to_response('car/info.html', context)