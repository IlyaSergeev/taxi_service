__author__ = 'hensh'

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from TaxiService.models import Car, Ride, User

#TODO refactoring. Extract all permission creators to disctionary + factory method

def get_permission_or_none(codename):
    try:
        return Permission.objects.get(codename=codename)
    except Permission.DoesNotExist:
        return None

def get_permission_view_users():
    permission_codename = "view_users"
    permission = get_permission_or_none(permission_codename)
    if permission is None:
        permission = Permission.objects.create(
            codename = permission_codename,
            name = 'Can view users',
            content_type = ContentType.objects.get_for_model(User),
        )
    return permission

def get_permission_view_cars():
    permission_codename = "view_cars"
    permission = get_permission_or_none(permission_codename)
    if permission is None:
        permission = Permission.objects.create(
            codename = permission_codename,
            name = 'Can view cars',
            content_type = ContentType.objects.get_for_model(Car),
        )
    return permission

def get_permission_view_rides():
    permission_codename = "view_rides"
    permission = get_permission_or_none(permission_codename)
    if permission is None:
        permission = Permission.objects.create(
            codename = permission_codename,
            name = 'Can view rides',
            content_type = ContentType.objects.get_for_model(Ride),
        )
    return permission

def get_permission_view_self_car():
    permission_codename = "view_self_car"
    permission = get_permission_or_none(permission_codename)
    if permission is None:
        permission = Permission.objects.create(
            codename = permission_codename,
            name = 'Can view self cars',
            content_type = ContentType.objects.get_for_model(Car),
        )
    return permission