__author__ = 'hensh'

from django.shortcuts import render_to_response
from django.template import RequestContext
from TaxiService.models import Car, Ride, Driver
from django.http import Http404
from dateutil import parser
from django.shortcuts import redirect
from TaxiService.required_group_test import group_required

def __fill_ride_from_post(ride, post):
    address_from = post.get('address_from')
    address_to = post.get('address_to')
    date = parser.parse(post.get('date'))
    ride.fromAddress = address_from
    ride.toAddress = address_to
    ride.date = date
    return ride

def __is_string_empty(string):
    return string is None or string is ''

def __is_ride_correct(ride):
    return not __is_string_empty(ride.fromAddress) and not __is_string_empty(ride.toAddress) and ride.car is not None and ride.date is not None

# TODO has problems with setting date to html file (NOW NOT USED)
@group_required('Dispatchers')
def edit(request, ride_id):
    try:
        ride = Ride.objects.get(id = ride_id)
    except Ride.DoesNotExist:
        return Http404

    if request.POST:
        __fill_ride_from_post(ride, request.POST).save()
        return redirect('car_rides', ride.car.id)

    context = RequestContext(
        request,
        {
            'car' : ride.car,
            'ride' : ride,
        },
    )
    return render_to_response('ride/edit.html', context)

@group_required('Dispatchers')
def create(request, car_id):
    try:
        car = Car.objects.get(id = car_id)
    except:
        return Http404

    if request.POST:
        ride =__fill_ride_from_post(Ride(car = car), request.POST)
        if __is_ride_correct(ride):
            ride.save()
            return redirect('car_rides', car_id)
        else:
            return redirect('ride_create')

    context = RequestContext(
        request,
        {
            'car' : car
        },
    )
    return render_to_response('ride/create.html', context)

def __get_rides_for_car(car_id, request):
    try:
        car = Car.objects.get(id = car_id)
    except Car.DoesNotExist:
        return Http404
    rides = Ride.objects.filter(car = car).order_by('date')
    context = RequestContext(
        request,
        {
            'rides' : rides,
            'car' : car,
        },
    )
    return render_to_response('ride/rides.html', context)

@group_required('Dispatchers')
def all_for_car(request, car_id):
    return __get_rides_for_car(car_id, request)

@group_required('Drivers')
def all_for_my_car(request, car_id):
    try:
        driver = Driver.objects.get(car_id = car_id)
    except Driver.DoesNotExist:
        return Http404
    if driver.account_id != request.user.id:
        return Http404
    return __get_rides_for_car(car_id, request)

@group_required('Dispatchers')
def delete(request, ride_id):
    try:
        ride = Ride.objects.get(id=ride_id)
    except Ride.DoesNotExist:
        return Http404

    ride.delete()

    return redirect('car_rides', ride.car.id)