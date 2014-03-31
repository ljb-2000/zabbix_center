from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
#from screens.models import Groups, HostsGroups, model_tests
from api_process.process import *
zabbix_url = process_base().zabbix_url

def spider_index(request):
	context = {'zabbix_url': zabbix_url}
	return render(request, 'spider/index.html', context)

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			cc_myself = form.cleaned_data['cc_myself']

			recipients = ['info@example.com']
			if cc_myself:
				recipients.append(sender)

			from django.core.mail import send_mail
			send_mail(subject, message, sender, recipients)

			return HttpResponseRedirect('/thanks/')
	else:
		form = ContactForm()

	return render(request, 'contact.html', {'form': form,})