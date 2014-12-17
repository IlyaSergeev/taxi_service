from django.conf.urls import  patterns, url

from TaxiService.views import views, account_views, car_views, ride_views

urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^home/$', views.home, name='home'),
    url(r'^accounts/login/$', views.login_user, name='login'),
    url(r'^accounts/logout/$', views.logout_user, name='logout'),

    url(r'^accounts/create/$', account_views.create, name='account_create'),
    url(r'^accounts/(?P<user_id>\d+)/$', account_views.account_info, name='account_info'),
    url(r'^accounts/(?P<user_id>\d+)/edit/$', account_views.account_edit, name='account_edit'),
    url(r'^accounts/$', account_views.accounts, name='accounts'),

    url(r'^cars/$', car_views.cars, name='cars'),
    url(r'^cars/create/$', car_views.mock1, name='car_create'),
    url(r'^cars/(?P<car_id>\d+/)/$', car_views.mock, name='car_info'),
    url(r'^cars/(?P<car_id>\d+/)/edit/$', car_views.mock, name='car_edit'),
    url(r'^cars/(?P<car_id>\d+/)/rides/$', car_views.mock, name='car_rides'),
    url(r'^cars/(?P<car_id>\d+/)/rides/create/$', car_views.mock, name='car_ride_create'),
    url(r'^cars/my/$', car_views.mock, name='my_car'),

    url(r'^rides/(?P<ride_id>\d+/)/$', ride_views.mock, name='ride_info'),
    url(r'^rides/(?P<ride_id>\d+/)/edit/$', ride_views.mock, name='ride_edit'),
)