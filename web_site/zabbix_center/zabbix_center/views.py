from django.shortcuts import render
from api_process.process import *

zabbix_url = process_base().zabbix_url
# Create your views here.
def Home(request):
    #latest_groups_list = Groups.objects.all()
	context = {'zabbix_url': zabbix_url}
	return render(request, 'base/index.html',context)