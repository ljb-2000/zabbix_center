from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from api_process.process import *
zabbix_url = process_base().zabbix_url

from snooze.forms import ackForm
import threading

def issue_detail(request):
	issues = last_issue().current_issues()
	context = {'issues': issues, 'zabbix_url': zabbix_url}

	return render(request, 'snooze/last_issues.html', context)

def snooze_process(request, trigger_id):

	if request.method == 'POST':
		form = ackForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data

			ack_text = cd['ack_text']
			snooze_time = cd['time_snoozes']
			snooze_time_h = process_base().clock_2_timedelta(int(snooze_time))

			result = last_issue().snoozeTimer(trigger_id, int(snooze_time))
			result.start()

			event_id = tid_process(trigger_id).tid2eid()
			
			#event_id = result['lastEvent']['eventid']
			last_issue().ack_process(event_id, ack_text)

			return render(request, 'snooze/result.html', {'zabbix_url': zabbix_url,
															'ack_text': ack_text,
															'event_id': event_id,
															'snooze_time_h': snooze_time_h})
	else:
		form = ackForm()

	context = {'zabbix_url': zabbix_url, 'form': form}
	return render(request, 'snooze/form.html', context)

			


