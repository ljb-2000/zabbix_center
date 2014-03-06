from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from screens.models import Groups

def index(request):
    latest_Groups_list = Groups.objects.all()
    context = {'latest_Groups_list': latest_Groups_list}
    return render(request, 'screens/index.html', context)

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'screens/detail.html', {'poll': poll})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)