# import zabbixAPI
from pyzabbix import ZabbixAPI
# The hostname at which the Zabbix web interface is available
ZABBIX_SERVER = 'http://192.168.1.203:82'
zapi = ZabbixAPI(ZABBIX_SERVER)
# Login to the Zabbix API
zapi.login('Admin', 'zabbix')

# return the name_list from hostgroup.get()
hostgroup_dic = zapi.hostgroup.get(output='extend')
# name_list is the all group name
name_list = [item['name'] for item in hostgroup_dic]

zapi.hostgroup.get(selectHosts='',output='extend',monitored_hosts=1)

