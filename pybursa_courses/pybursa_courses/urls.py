from django.conf.urls import patterns, include, url
from django.contrib import admin

from pybursa_courses import view

urlpatterns = patterns('',

    url(r'^$', view.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^students/', include('students.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^coaches/', include('coaches.urls')),
)
