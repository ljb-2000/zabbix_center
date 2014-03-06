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

from polls import views

urlpatterns = patterns('',
	# ex: /polls/
	url(r'^$', views.index, name='index'),
	# ex: /polls/5/
	url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)