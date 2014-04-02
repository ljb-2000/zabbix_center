from django.shortcuts import render, get_object_or_404, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
#from screens.models import Groups, HostsGroups, model_tests
from api_process.process import *
zabbix_url = process_base().zabbix_url

from spider.forms import ContactForm, addHostsForm



def spider_index(request):
    if request.method == 'POST':
        form = addHostsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # use zapi add host
            hosts = cd['hosts'].split()
            group = cd['group']
            templateids = cd['templateids']

            response=[]
            for host in hosts:
                test = Spider().addHosts(host, group, templateids)
                response.append(test)
            return render(request, 'spider/form_response.html', {'zabbix_url': zabbix_url 
                                                                 'response': response})
    else:
        form = addHostsForm()

    context = {'zabbix_url': zabbix_url, 'form': form}
    return render(request, 'spider/index.html', context)


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            message = 'You searched for: %r' % q
            return render_to_response('spider/search_form.html', {'query': message})
    return render_to_response('spider/search_form.html', {'errors': errors})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # send_mail(
#                cd['subject'],
#                cd['message'],
#                cd.get('email', 'noreply@example.com'),
#                ['siteowner@example.com'],
#            )
            return render_to_response('spider/contact_form.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = ContactForm()

    return render_to_response('spider/contact_form.html', {'form': form}, context_instance=RequestContext(request))


def contact_bak(request):
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

            return HttpResponseRedirect('/spider/thanks/')
    else:
        form = ContactForm()

    return render(request, '/spider/contact.html', {'form': form, })
