from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from TaxiService.user_groups import *
from TaxiService.models import *
from django.shortcuts import redirect

def login_user(request):
    if request.user.is_authenticated():
        return redirect('home')
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if (user is not None):
            if user.is_active:
                login(request, user)
                return redirect('home')
    context = RequestContext(request)
    context.update(csrf(request))
    return render_to_response('account/login.html', context)


def logout_user(request):
    logout(request)
    return render_to_response('home.html', RequestContext(request))


def home(request):
    return render_to_response('home.html', RequestContext(request))

def init_test_data(request):
    if request.POST:
        __add_test_info()
        redirect('home')
    return render_to_response('init_test_data.html', RequestContext(request))

def __add_test_info():
    admin_kate = User(
        username = 'kate',
        email = 'kate@taxi-service.com',
        password = 'qwe',
    )
    admin_kate.save()
    admin_kate.groups.add(get_group_admin())

    dispatcher_bob = User(
        username = 'bob',
        email = 'bob@taxi-service.com',
        password = 'qwe',
    )
    dispatcher_bob.save()
    dispatcher_bob.groups.add(get_group_dispatcher())

    driver_alex = User(
        username = 'alex',
        email = 'alex@taxi-service.com',
        password = 'qwe',
    )
    driver_alex.save()
    driver_alex.groups.add(get_group_driver())

    driver_john = User(
        username = 'john',
        email = 'john@taxi-service.com',
        password = 'qwe',
    )

    driver_john.save()
    driver_john.groups.add(get_group_driver())

    driver_anne = User(
        username = 'anne',
        email = 'anne@taxi-service.com',
        password = 'qwe',
    )
    driver_anne.save()
    driver_anne.groups.add(get_group_driver())

    car_mercedes = Car(
        brand = 'mercedes',
        model = 'slk',
        color = 'silver',
        reg_number = 'ay001p'
    )
    car_mercedes.save()
    __add_some_rides(car_mercedes, 10)

    car_bmw = Car(
        brand = 'bmw',
        model = 'x5',
        color = 'black',
        reg_number = 'ay002p'
    )
    car_bmw.save()
    __add_some_rides(car_bmw, 4)

    car_lada = Car(
        brand = 'Lada',
        model = '2108',
        color = 'white in apples',
        reg_number = 'ay003p'
    )
    car_lada.save()
    __add_some_rides(car_lada, 43)

    car_toyota = Car(
        brand = 'Toyota',
        model = 'camry',
        color = 'light blue',
        reg_number = 'ay004p'
    )
    car_toyota.save()
    __add_some_rides(car_toyota, 13)

    Driver(
        account = driver_alex,
        car = car_mercedes,
    ).save()

    Driver(
        account = driver_anne,
        car = car_toyota,
    ).save()

def __add_some_rides(car, history_len):
    import datetime
    date = datetime.datetime.now() - datetime.timedelta(hours=3*(history_len+1))
    for i in range(0, history_len):
        Ride(
          car = car,
          fromAddress = "some from address " + str(i),
          toAddress = "some to address " + str(i),
          date = date
        ).save()
        date += datetime.timedelta(hours=1)
