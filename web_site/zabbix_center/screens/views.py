from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from screens.models import Groups, HostsGroups, model_tests
from screens.process import gid_process


def group_index(request):
    #latest_groups_list = Groups.objects.all()
	context = {'latest_groups_list': gid_process().gid_2_group_list()}
	return render(request, 'screens/group_index.html', context)


def grouphost_detail(request, group_id):
	group_name = gid_process().gid_2_group(group_id)
	host_list = gid_process().gid_2_host(group_id)
	context = {'groups': group_name , 'host_list': host_list}
	return render(request, 'screens/grouphost_detail.html', context)


def hostgraph_detail(request, host_id):
	graphs = zapi.host.get(hostid=host_id, selectGraphs='')
	context = {'graphs': graphs}
	return render(request, 'screens/hostgraphs.html', context)


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