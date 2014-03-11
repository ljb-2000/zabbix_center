from django.db import models

# Create your models here.
# import MySQLdb 
import MySQLdb as mdb


class Groups(models.Model):
	group_name = models.CharField(max_length=64)

	def __unicode__(self):
		return self.group_name

class HostsGroups(models.Model):
	group = models.ForeignKey(Groups)
	hosts = models.CharField(max_length=64)

	def __unicode__(self):
		return self.hosts

class HostsGroups(models.Model):
	hosts = models.ForeignKey(HostsGroups)
	graphid = models.IntegerField(default=0)

	def __unicode__(self):
		return self.hosts


def model_tests(user, password, database, host='localhost'):

	db = mdb.connect(host=host, user=user, passwd=password, db=database)

	with db:
		cur = db.cursor()
		query_sql = '''select a.name, a.groupid, b.hostid, c.host from 
		groups a, 
		hosts_groups b, 
		hosts c 
		where a.groupid = b.groupid 
		and b.hostid = c.hostid;'''

		cur.execute(query_sql)
		result = cur.fetchall()

		return result
