from django.contrib import admin
from polls.models import Poll, Choice
# Register your models here.

class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 3

	list_display = ('question', 'pub_date')

class PollAdmin(admin.ModelAdmin):
	filedsets = [
		(None, 					{'fields':['question']}),
		('Date information', 	{'fields':['pub_date']}),
	]
	inlines = [ChoiceInline]

	list_display=('question', 'pub_date', 'was_published_recently')

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
