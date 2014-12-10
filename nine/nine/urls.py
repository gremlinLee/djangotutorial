from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^square/', include('square.urls', namespace="square")),
    url(r'^heroes/', include('heroes.urls', namespace="heroes"))
)
