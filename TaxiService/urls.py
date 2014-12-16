from django.conf.urls import  patterns, url

from TaxiService.views import views, account_views, car_views, ride_views, dispatcher_views, driver_views

urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^home/$', views.home, name='home'),
    url(r'^accounts/login/$', views.login_user, name='login'),
    url(r'^accounts/logout/$', views.logout_user, name='logout'),

    url(r'^accounts/create/$', account_views.create, name='create_account'),
    url(r'^accounts/(?P<user_id>\d+)/$', account_views.account_info, name='account_info'),
    url(r'^accounts/(?P<user_id>\d+)/edit/$', account_views.account_edit, name='edit_account'),
    url(r'^accounts/$', account_views.accounts, name='accounts'),

    url(r'^cars/', car_views.mock, name='car_mock'),
    url(r'^rides/', ride_views.mock, name='ride_mock'),
)