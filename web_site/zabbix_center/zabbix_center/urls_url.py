from django.conf.urls import patterns, url

from zabbix_center import views

urlpatterns = patterns('',
	# ex: /polls/
	url(r'^$', views.Home, name='Home'),
)