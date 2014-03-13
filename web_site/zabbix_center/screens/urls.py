#from __future__ import unicode_literals
#from django.conf.urls import patterns, url
#from django.views.generic import TemplateView

#from screens.views import *

#urlpatterns = patterns('',
    #url(r'^$', HomePageView.as_view(), name='home'),
    #url(r'^form$', FormView.as_view(), name='form'),
    #url(r'^form_horizontal$', FormHorizontalView.as_view(), name='form_horizontal'),
    #url(r'^form_inline$', FormInlineView.as_view(), name='form_inline'),
    #url(r'^pagination$', PaginationView.as_view(), name='pagination'),
    #url(r'^bootstrap$', BootstrapView.as_view(), name='bootstrap'),
    #url(r'^check$', CheckView.as_view(), name='check'),
#)

from django.conf.urls import patterns, url

from screens import views

urlpatterns = patterns('',
	# ex: /polls/
	url(r'^$', views.group_index, name='group_index'),
	# ex: /polls/5/
	url(r'^(?P<group_id>\d+)/$', views.grouphost_detail, name='grouphost_detail'),
    url(r'^tests', views.tests, name='tests'),
    url(r'^(?P<host_id>\d+)/$', views.hostgraph_detail, name='hostgraph_detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<group_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<group_id>\d+)/vote/$', views.vote, name='vote'),
)