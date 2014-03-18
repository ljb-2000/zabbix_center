# import zabbixAPI
from pyzabbix import ZabbixAPI
# The hostname at which the Zabbix web interface is available

# input groupid 
# output host and hostid in {'host': host, 'hostid': hostid}
class process_base(object):
	def __init__(self):
		ZABBIX_SERVER = 'http://192.168.1.203:82'
		#ZABBIX_SERVER = 'http://119.79.232.99:82'
		self.zapi = ZabbixAPI(ZABBIX_SERVER)
		# Login to the Zabbix API
		self.zapi.login('Admin', 'zabbix')


	def gid_2_group_list(self):
		'''
		'''
		return self.zapi.hostgroup.get(output='extend')


class gid_process(process_base):
	def __init__(self, group_id):
		process_base.__init__(self)
		self.group_id = group_id


	def gid2host_filter(self):
		'''
		'''
		hostgroup_dic = self.zapi.hostgroup.get(output='extend', selectHosts='')
		for item in hostgroup_dic:
			if self.group_id == item['groupid']:
				return item

	def gid_2_host(self):
		'''
		'''
		host_list = self.gid2host_filter()

		for i in host_list['hosts']:
			i['host'] = self.zapi.host.get(filter={'hostid':i['hostid']}, output='extend')[0]['name']

		return host_list['hosts']


	def gid_2_group(self):
		'''
		'''
		return self.zapi.hostgroup.getobjects(groupid=self.group_id)

	
class hid_process(process_base):
	def __init__(self, host_id):
		process_base.__init__(self)
		self.host_id = host_id


	def hid_2_graph_list(self):
		'''
		'''
		temp_result = self.zapi.graph.get(hostids=self.host_id, output='extend')
		test_1 = [{'name': i['name'], 'graphid':i['graphid'], 'group': i['name'].split()[0]} for i in temp_result]
		test_list = {}.fromkeys([item['group'] for item in test_1]).keys()
		result_list = [{'name': item , 'content':[]} for item in test_list]
		for x in result_list:
			for i in test_1:
				if i['group'] == x['name']:
					x['content'].append({'graphid': i['graphid'], 'name': i['name']})

		return result_list

