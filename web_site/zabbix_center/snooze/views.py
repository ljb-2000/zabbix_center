from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from api_process.process import *
zabbix_url = process_base().zabbix_url

def issue_detail(request):
	issues = last_issue().current_issues()
	context = {'issues': issues, 'zabbix_url': zabbix_url}

	return render(request, 'snooze/last_issues.html', context)