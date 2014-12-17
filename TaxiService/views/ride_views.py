__author__ = 'hensh'

from django.shortcuts import render_to_response
from TaxiService.required_group_test import group_required
from django.template import RequestContext

def mock(request):
    return render_to_response('ride/mock.html', RequestContext(request))