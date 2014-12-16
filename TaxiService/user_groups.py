__author__ = 'hensh'

from django.contrib.auth.models import Group
from permissions import *

def getGroupOrNone(groupName):
    try:
        return Group.objects.get(name = groupName)
    except Group.DoesNotExist:
        return None

admin_group_name = "Admins"
admin_group =  getGroupOrNone(admin_group_name)
if admin_group is None:
    admin_group = Group(name = admin_group_name)
    admin_group.save()
    admin_group.permissions.add(
        Permission.objects.get(codename='change_user'),
        Permission.objects.get(codename='delete_user'),
        Permission.objects.get(codename='add_user'),
        Permission.objects.get(codename='change_car'),
        Permission.objects.get(codename='delete_car'),
        Permission.objects.get(codename='add_car'),
        get_permission_view_users(),
    )

dispatcher_group_name = "Dispatchers"
dispatcher_group = getGroupOrNone(dispatcher_group_name)
if dispatcher_group is None:
    dispatcher_group = Group(name = dispatcher_group_name)
    dispatcher_group.save()
    dispatcher_group.permissions.add(
        Permission.objects.get(codename='change_ride'),
        Permission.objects.get(codename='delete_ride'),
        Permission.objects.get(codename='add_ride'),
        get_permission_view_cars(),
        get_permission_view_rides(),
    )


driver_group_name = "Drivers"
driver_group = getGroupOrNone(driver_group_name)
if driver_group is None:
    driver_group = Group(name = driver_group_name)
    driver_group.save()
    driver_group.permissions.add(
        get_permission_view_rides(),
        get_permission_view_self_car(),
    )

