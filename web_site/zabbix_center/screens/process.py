# import zabbixAPI
from pyzabbix import ZabbixAPI
# The hostname at which the Zabbix web interface is available

# input groupid 
# output host and hostid in {'host': host, 'hostid': hostid}
class gid_process(object):
	def __init__(self):
		#ZABBIX_SERVER = 'http://192.168.1.204'
		ZABBIX_SERVER = 'http://119.97.226.138:82'
		self.zapi = ZabbixAPI(ZABBIX_SERVER)
		# Login to the Zabbix API
		self.zapi.login('Admin', 'zabbix')

	def gid_2_host(self, group_id):
		'''
		'''
		hostgroup_dic = self.zapi.hostgroup.get(output='extend', selectHosts='')
		for item in hostgroup_dic:
			if group_id == item['groupid']:
				group_item = item

		host_list = group_item['hosts']

		for i in host_list:
			i['host'] = self.zapi.host.get(filter={'hostid':i['hostid']}, output='extend')[0]['name']

		return host_list

	def gid_2_group(self, group_id):
		'''
		'''
		return self.zapi.hostgroup.getobjects(groupid=group_id)[0]['name']

	def gid_2_group_list(self):
		'''
		'''
		return self.zapi.hostgroup.get(output='extend')

