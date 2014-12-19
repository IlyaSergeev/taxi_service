__author__ = 'hensh'

from django.shortcuts import render_to_response
from django.template import RequestContext
from TaxiService.models import Car, Ride
from django.http import Http404
from dateutil import parser
from django.shortcuts import redirect

def edit(request, ride_id):
    return render_to_response('ride/edit.html', RequestContext(request))

def create(request, car_id):
    try:
        car = Car.objects.get(id = car_id)
    except:
        return Http404

    if request.POST:
        address_from = request.POST.get('address_from')
        address_to = request.POST.get('address_to')
        date = parser.parse(request.POST.get('date'))
        ride = Ride(
            fromAddress = address_from,
            toAddress = address_to,
            date = date,
            car = car
        )
        ride.save()
        return redirect('car_rides', car_id)

    context = RequestContext(
        request,
        {
            'car' : car
        },
    )
    return render_to_response('ride/create.html', context)

def all_for_car(request, car_id):
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

def delete(request, ride_id):
    try:
        ride = Ride.objects.get(id=ride_id)
    except Ride.DoesNotExist:
        return Http404

    ride.delete()

    return redirect('car_rides', ride.car.id)