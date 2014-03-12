from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from screens.models import Groups, HostsGroups, model_tests

# import zabbixAPI
from pyzabbix import ZabbixAPI
# The hostname at which the Zabbix web interface is available
#ZABBIX_SERVER = 'http://192.168.1.204'
ZABBIX_SERVER = 'http://119.97.226.138:82'
zapi = ZabbixAPI(ZABBIX_SERVER)
# Login to the Zabbix API
zapi.login('Admin', 'zabbix')

# return the name_list from hostgroup.get()
hostgroup_dic = zapi.hostgroup.get(output='extend', selectHosts='')


def group_index(request):
    #latest_groups_list = Groups.objects.all()
	context = {'latest_groups_list': hostgroup_dic}
	return render(request, 'screens/group_index.html', context)


def grouphost_detail(request, groupid):
	for item in hostgroup_dic:
		if groupid == item['groupid']:
			group = item

	hostids = [item_in['hostid'] for item_in in group['hosts']]
	hostid_list = []
	for host_id in hostids:         
		hostid_list.append(zapi.host.get(filter={'hostid':host_id}, output='extend')[0]['name'])

	context = {'groups': group , 'host_list': hostid_list, 'hostid_list':hostids}
	return render(request, 'screens/grouphost_detail.html', context)


def hostview(request, hostid):

	return render(request, 'screens/hosts.html', context)


def tests(request):
	#context = {'result': model_tests('root','123456','zabbix')}
	test_dic_test = [{'test_inside1': 'test_inside1'},{'test_inside2':'test_inside2'}]
	test_dic = {'test1':'test1', 'test2':'test2', 'test3':'test3', 'test4':test_dic_test}
	context = {'result': test_dic}
	return render(request, 'screens/tests.html', context)

#def results(request, group_id):
#    return HttpResponse("You're looking at the results of group %s." % group_id)

#def vote(request, group_id):
#    return HttpResponse("You're voting on groups %s." % group_id)