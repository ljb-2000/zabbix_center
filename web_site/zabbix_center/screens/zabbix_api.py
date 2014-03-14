# import zabbixAPI
from pyzabbix import ZabbixAPI
# The hostname at which the Zabbix web interface is available
#ZABBIX_SERVER = 'http://119.97.226.138:82'
ZABBIX_SERVER = 'http://192.168.1.204'
zapi = ZabbixAPI(ZABBIX_SERVER)
# Login to the Zabbix API
zapi.login('Admin', 'zabbix')

# return the name_list from hostgroup.get()
hostgroup_dic = zapi.hostgroup.get(output='extend')
# name_list is the all group name
name_list = [item['name'] for item in hostgroup_dic]

result = zapi.hostgroup.get(selectHosts='',output='extend',monitored_hosts=1)

# 
result_dic = {}

for item in result:
    result_dic[item['name']] = [item_in['hostid'] for item_in in item['hosts']]

In [49]: d = {x: zapi.host.get(filter={'hostid':x}, output='extend')[0]['name'] for x in hostids}

In [50]: d
Out[50]: 
{u'10237': u'117.135.138.38',
 u'10238': u'117.135.138.36',
 u'10239': u'117.135.138.248',
 u'10240': u'117.135.138.196',
 u'10241': u'117.135.139.30',
 u'10242': u'117.135.139.237'}

 <a href="{% url 'screens:hostgraph_detail' host_name %}">{{ host_name }}</a>