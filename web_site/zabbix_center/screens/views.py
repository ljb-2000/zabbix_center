from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from screens.models import Groups, HostsGroups, model_tests
from api_process.process import *

zabbix_url = process_base().zabbix_url

def group_index(request):
    #latest_groups_list = Groups.objects.all()
	context = {'latest_groups_list': process_base().gid_2_group_list(),
				'zabbix_url': zabbix_url}
	return render(request, 'screens/group_index.html', context)


def grouphost_detail(request, group_id):
	group = gid_process(group_id).gid_2_group()
	host_list = gid_process(group_id).gid_2_host()
	context = {'groups': group , 'host_list': host_list}
	return render(request, 'screens/grouphost_detail.html', context)


def hostgraph_detail(request, host_id):
	graphs = hid_process(host_id).hid_2_graph_list()
	hosts = hid_process(host_id).hid_2_host_name()
	context = {'graphs': graphs, 'hosts': hosts, 'zabbix_url': zabbix_url}
	return render(request, 'screens/hostgraphs.html', context)


#def issue_detail(request):
#	issues = last_issue().current_issues()
#	context = {'issues': issues, 'zabbix_url': zabbix_url}

#	return render(request, 'screens/last_issues.html', context)


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