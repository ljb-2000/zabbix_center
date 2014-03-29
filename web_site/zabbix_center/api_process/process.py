# import zabbixAPI
from pyzabbix import ZabbixAPI
from datetime import datetime
# The hostname at which the Zabbix web interface is available

# input groupid
# output host and hostid in {'host': host, 'hostid': hostid}


class process_base(object):

    def __init__(self):
        #ZABBIX_SERVER = 'http://192.168.1.203:82'
        ZABBIX_SERVER = 'http://119.79.232.99:82'
        self.zapi = ZabbixAPI(ZABBIX_SERVER)
        # Login to the Zabbix API
        self.zapi.login('Admin', 'zabbix')
        self.zabbix_url = ZABBIX_SERVER

    def gid_2_group_list(self):
        '''
        '''
        return self.zapi.hostgroup.get(output='extend')

    def zabbix_url(self):
        # just for view.py intial the zabbix_url
        return self.zabbix_url

    def clock_2_time(self, clock_time):
        '''
        '''
        return datetime.fromtimestamp(int(clock_time)).strftime('%Y-%m-%d %X')

    def clock_2_timedelta(self, clock_time):
        '''

        '''
        time_delta = datetime.fromtimestamp(
            int(clock_time)) - datetime.fromtimestamp(0)
        delta_day = time_delta.days
        delta_hour = time_delta.seconds / 3600
        delta_min = time_delta.seconds % 3600 / 60
        return '%s days, %s hours, %s minutes' % (delta_day, delta_hour, delta_min)


class gid_process(process_base):

    def __init__(self, group_id):
        process_base.__init__(self)
        self.group_id = group_id

    def gid2host_filter(self):
        '''
        '''
        hostgroup_dic = self.zapi.hostgroup.get(
            output='extend', selectHosts='')
        for item in hostgroup_dic:
            if self.group_id == item['groupid']:
                return item

    def gid_2_host(self):
        '''
        '''
        host_list = self.gid2host_filter()

        for i in host_list['hosts']:
            i['host'] = self.zapi.host.get(
                filter={'hostid': i['hostid']}, output='extend')[0]['name']
            temp = self.zapi.item.get(
                hostids=i['hostid'], output='extend', search={'name': '_info'})
            for item in temp:
                if 'host boot time' in item['name'].lower():
                    # system boot time
                    i['boot_time'] = self.clock_2_time(item['lastvalue'])
                elif 'cpu numbers' in item['name'].lower():
                    # cpu numbers
                    i['cpu_number'] = item['lastvalue']
                elif 'host name' in item['name'].lower():
                    # host name
                    i['host_name'] = item['lastvalue']
                elif 'cpu model' in item['name'].lower():
                    # cpu model
                    i['cpu_model'] = item['lastvalue']
                elif 'system information' in item['name'].lower():
                    # kernel model
                    i['kernel_info'] = item['lastvalue'].split()[2]
                elif 'system uptime' in item['name'].lower():
                    # system uptime
                    i['uptime'] = self.clock_2_timedelta(item['lastvalue'])
                elif 'total memory' in item['name'].lower():
                    # total memory size
                    i['total_memory'] = int(item['lastvalue']) / 1024 / 1024
                else:
                    pass

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
        temp_result = self.zapi.graph.get(
            hostids=self.host_id, output='extend')
        test_1 = [{'name': i['name'], 'graphid':i['graphid'],
                   'group': i['name'].split()[0]} for i in temp_result]
        test_list = {}.fromkeys([item['group'] for item in test_1]).keys()
        result_list = [{'name': item, 'content': []} for item in test_list]
        for x in result_list:
            for i in test_1:
                if i['group'] == x['name']:
                    x['content'].append(
                        {'graphid': i['graphid'], 'name': i['name']})

        return result_list

    def hid_2_host_name(self):
        '''
        '''
        return self.zapi.host.get(hostids=self.host_id, output='extend')


class last_issue(process_base):

    def __init__(self):
        process_base.__init__(self)

    def current_issues(self):
        '''
        [{u'comments': u'',
        u'description': u'Zabbix poller processes more than 75% busy',
          u'error': u'',
          u'expression': u'({TRIGGER.VALUE}=0&{13124}>75)|({TRIGGER.VALUE}=1&{13124}>65)',
          u'flags': u'0',
          u'host': u'Zabbix server',
          u'hostid': u'10084',
          u'hostname': u'Zabbix server',
          u'items': [{u'itemid': u'23264'}],
          u'lastchange': u'1395215684',
          u'priority': u'3',
          u'state': u'0',
          u'status': u'0',
          u'templateid': u'13091',
          u'triggerid': u'13479',
          u'type': u'0',
          u'url': u'',
          u'value': u'0',
          u'value_flag': u'0'}]
        '''
        # Get a list of all issues (AKA tripped triggers)
        triggers = self.zapi.trigger.get(only_true=1,
                                         skipDependent=1,
                                         monitored=1,
                                         active=1,
                                         output='extend',
                                         expandDescription=1,
                                         expandData='host',
                                         selectItems='',
                                         selectLastEvent='',
                                         )
        trigger = [item for item in triggers if item['value'] == '1']
        return trigger
