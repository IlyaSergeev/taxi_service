from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'first_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls.py')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('TaxiService.urls'))
)
