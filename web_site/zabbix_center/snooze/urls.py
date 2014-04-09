from django.conf.urls import patterns, url

from snooze import views

urlpatterns = patterns('',
	# ex: /polls/
	# url(r'^$', views.group_index, name='group_index'),
	# ex: /polls/5/s
    url(r'^last_issue/$', views.issue_detail, name='issue_detail'),
    url(r'^ack/(?P<triggerid>\d+)/$', views.ack_process, name='ack_process'),
    # ex: /polls/5/results/
    #url(r'^(?P<group_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<group_id>\d+)/vote/$', views.vote, name='vote'),
)