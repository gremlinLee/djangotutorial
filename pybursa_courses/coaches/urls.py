from django.conf.urls import patterns, url
from coaches import views

urlpatterns = patterns('',
    url(r'^$', views.CoachListView.as_view(), name='coaches'),
    url(r'^(?P<pk>\d+)/$', views.ConcreteCoach.as_view(), name='coach'),
)