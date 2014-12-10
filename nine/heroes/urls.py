from django.conf.urls import patterns, url
from heroes import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<hero>\w+)', views.detail, name='detail')
)