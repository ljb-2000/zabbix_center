from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from screens.models import Groups, HostsGroups

# import zabbixAPI
from pyzabbix import ZabbixAPI
# The hostname at which the Zabbix web interface is available
ZABBIX_SERVER = 'http://192.168.1.203:82'
zapi = ZabbixAPI(ZABBIX_SERVER)
# Login to the Zabbix API
zapi.login('Admin', 'zabbix')

# return the name_list from hostgroup.get()
hostgroup_dic = zapi.hostgroup.get(output='extend')


def index(request):
    #latest_groups_list = Groups.objects.all()
    context = {'latest_groups_list': hostgroup_dic}
    return render(request, 'screens/index.html', context)

def detail(request, group_name):
    groups = result
    return render(request, 'screens/detail.html', {'groups': groups})

#def results(request, group_id):
#    return HttpResponse("You're looking at the results of group %s." % group_id)

#def vote(request, group_id):
#    return HttpResponse("You're voting on groups %s." % group_id)