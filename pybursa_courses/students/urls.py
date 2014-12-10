from django.conf.urls import patterns, url
from students import views

urlpatterns = patterns('',
    url(r'^$', views.StudentListView.as_view(), name='students'),
    url(r'^(?P<student_id>\d+)/$', views.concrete_student, name='student'),
)