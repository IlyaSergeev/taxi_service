__author__ = 'hensh'

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from TaxiService.models import *

def getPermitionOrNone(codename):
    try:
        return Permission.objects.get(codename=codename)
    except Permission.DoesNotExist:
        return None

view_users_permission_codename = "view_users"
def get_view_users_permission():
    permission = getPermitionOrNone(view_users_permission_codename)
    if permission is None:
        permission = Permission.objects.create(
            codename = view_users_permission_codename,
            name = 'Can view users',
            content_type = ContentType.objects.get_for_model(User),
        )
    return permission

view_cars_permission_codename = "view_cars"
def get_view_cars_permission():
    permission = getPermitionOrNone(view_cars_permission_codename)
    if permission is None:
        permission = Permission.objects.create(
            codename = view_cars_permission_codename,
            name = 'Can view cars',
            content_type = ContentType.objects.get_for_model(Car),
        )
    return permission

view_rides_permission_codename = "view_rides"
def get_view_rides_permission():
    permission = getPermitionOrNone(view_rides_permission_codename)
    if permission is None:
        permission = Permission.objects.create(
            codename = view_rides_permission_codename,
            name = 'Can view rides',
            content_type = ContentType.objects.get_for_model(Ride),
        )
    return permission

view_self_car_permission_codename = "view_self_car"
def get_view_self_car_permission():
    permission = getPermitionOrNone(view_self_car_permission_codename)
    if permission is None:
        permission = Permission.objects.create(
            codename = view_rides_permission_codename,
            name = 'Can view self cars',
            content_type = ContentType.objects.get_for_model(Car),
        )
    return permission