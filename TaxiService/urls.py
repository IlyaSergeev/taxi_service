from django.conf.urls import  patterns, url

from TaxiService import  views

urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^home/$', views.home, name='home'),
    url(r'^accounts/login/$', views.login_user, name='login'),
    url(r'^accounts/logout/$', views.logout_user, name='logout'),
    url(r'^accounts/signup/$', views.signup, name='signup'),
)