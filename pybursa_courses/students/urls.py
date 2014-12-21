from django.conf.urls import patterns, url
from students import views

urlpatterns = patterns('',
    url(r'^$', views.StudentListView.as_view(), name='students'),
    url(r'^(?P<student_id>\d+)/$', views.concrete_student, name='student'),
    url(r'^create_student/$', views.student_add, name='create_student'),
    url(r'^save_student/$', views.student_save, name='save_student'),
)