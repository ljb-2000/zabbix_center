from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
#from screens.models import Groups, HostsGroups, model_tests
from api_process.process import *
zabbix_url = process_base().zabbix_url

def spider_index(request):
	context = {'zabbix_url': zabbix_url}
	return render(request, 'spider/index.html', context)
