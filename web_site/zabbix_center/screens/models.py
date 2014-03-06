from django.db import models

# Create your models here.

class Groups(models.Model):
	group_name = models.CharField(max_length=64)

	def __unicode__(self):
		return self.group_name

class HostsGroups(models.Model):
	group = models.ForeignKey(Groups)
	hosts = models.CharField(max_length=64)

	def __unicode__(self):
		return self.hosts