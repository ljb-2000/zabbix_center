from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zabbix_center.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    # bootstrap demo
    url(r'^demo/', include('demo.urls', namespace="demo")),
    url(r'^demo_test/', include('demo_test.urls', namespace="demo_test")),
    url(r'^zabbix_tables/', include('zabbix_tables.urls', namespace="zabbix_tables")),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
		url(r'', include('django.contrib.staticfiles.urls')),
	)
