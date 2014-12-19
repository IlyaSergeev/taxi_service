__author__ = 'hensh'

from django.shortcuts import render_to_response
from django.template import RequestContext
from TaxiService.models import Driver, User, Car
from TaxiService.required_group_test import group_required
from TaxiService.user_groups import get_group_driver
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect

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
def edit(request, user_id):
    try:
        user = User.objects.get(id = user_id)
    except Driver.DoesNotExist:
        return Http404
    cur_car = None
    try:
        driver = Driver.objects.get(account = user)
        cur_car = driver.car
    except Driver.DoesNotExist:
        driver = None

    if request.POST:
        # TODO save all changes
        if driver is None:
            driver = Driver(account = user)

        car_id = request.POST.get('cars')
        try:
            car = Car.objects.get(id = car_id)
        except Car.DoesNotExist:
            car = None
        driver.car = car
        driver.save()

        return redirect('drivers')

    # TODO make this by single SQL request
    free_cars = list(Car.objects.all())
    drivers = Driver.objects.all()
    for driver in drivers:
        if driver.car in free_cars and driver.car != cur_car:
            free_cars.remove(driver.car)
    context = RequestContext(
        request,
        {
            'cur_user' : user,
            'cur_car' : cur_car,
            'free_cars' : free_cars
        }
    )
    return render_to_response('driver/edit.html', context)