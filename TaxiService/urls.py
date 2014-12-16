from django.conf.urls import  patterns, url

from TaxiService.views import views, admin_views, dispatcher_views, driver_views

urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^home/$', views.home, name='home'),
    url(r'^accounts/login/$', views.login_user, name='login'),
    url(r'^accounts/logout/$', views.logout_user, name='logout'),

    url(r'^accounts/signup/$', admin_views.signup, name='signup'),
    url(r'^accounts/$', admin_views.accounts, name='accounts'),
)