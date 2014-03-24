from __future__ import unicode_literals
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from zabbix_tables.views import *

urlpatterns = patterns('',
	url(r'^$', TableView.as_view(), name='home'), 
)