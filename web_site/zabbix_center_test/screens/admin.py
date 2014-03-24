from django.contrib import admin
from screens.models import Groups, HostsGroups
# Register your models here.

class HostsInline(admin.StackedInline):
	model = HostsGroups
	extra = 3


class GroupsAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 		{'fields':['group_name']}),
	]
	inlines = [HostsInline]
	list_display = ('group_name',)

admin.site.register(Groups, GroupsAdmin)
