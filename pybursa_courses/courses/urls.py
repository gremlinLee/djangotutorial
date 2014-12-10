from django.conf.urls import patterns, url
from courses import views

urlpatterns = patterns('',
    url(r'^$', views.CourseListView.as_view(), name='courses'),
    url(r'^(?P<course_id>\d+)/$', views.concrete_course, name='course'),
)