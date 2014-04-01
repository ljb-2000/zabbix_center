from django.conf.urls import patterns, url

from spider import views

urlpatterns = patterns('',
	# ex: /polls/
	url(r'^$', views.spider_index, name='spider_index'),
    (r'^search/$', views.search),
    (r'^contact/$', views.contact),
	# ex: /polls/5/
	#url(r'^hostgroup/(?P<group_id>\d+)/$', views.grouphost_detail, name='grouphost_detail'),
    #url(r'^tests', views.tests, name='tests'),
    #url(r'^hostgraph/(?P<host_id>\w+)/$', views.hostgraph_detail, name='hostgraph_detail'),
    #url(r'^last_issue/$', views.issue_detail, name='issue_detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<group_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<group_id>\d+)/vote/$', views.vote, name='vote'),
)