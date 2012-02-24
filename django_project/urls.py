from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

from main.views import generic_view

urlpatterns = patterns('',
    url(r'^$',generic_view, {'template_name':'home.shpaml'},name='home'), 

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
admin.autodiscover()
