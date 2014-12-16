__author__ = 'hensh'

from django.contrib.auth.models import Group
from permissions import *

def __getGroupOrNone(groupName):
    try:
        return Group.objects.get(name = groupName)
    except Group.DoesNotExist:
        return None


def get_group_admin():
    group_name = "Admins"
    group = __getGroupOrNone(group_name)
    if group is None:
        group = Group(name = group_name)
        group.save()
        group.permissions.add(
            Permission.objects.get(codename='change_user'),
            Permission.objects.get(codename='delete_user'),
            Permission.objects.get(codename='add_user'),
            Permission.objects.get(codename='change_car'),
            Permission.objects.get(codename='delete_car'),
            Permission.objects.get(codename='add_car'),
            get_permission_view_users(),
        )
    return  group

def get_group_dispatcher():
    group_name = "Dispatchers"
    group = __getGroupOrNone(group_name)
    if group is None:
        group = Group(name = group_name)
        group.save()
        group.permissions.add(
            Permission.objects.get(codename='change_ride'),
            Permission.objects.get(codename='delete_ride'),
            Permission.objects.get(codename='add_ride'),
            get_permission_view_cars(),
            get_permission_view_rides(),
        )
    return group

def get_group_driver():
    group_name = "Drivers"
    group = __getGroupOrNone(group_name)
    if group is None:
        group = Group(name = group_name)
        group.save()
        group.permissions.add(
            get_permission_view_rides(),
            get_permission_view_self_car(),
        )
    return group