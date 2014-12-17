from django.conf.urls import patterns, include, url
from django.contrib import admin

from pybursa_courses import view

urlpatterns = patterns('',

    url(r'^$', view.index, name='index'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^students/', include('students.urls'), name='students'),
    url(r'^courses/', include('courses.urls'), name='courses'),
    url(r'^coaches/', include('coaches.urls'), name='coaches'),
)
