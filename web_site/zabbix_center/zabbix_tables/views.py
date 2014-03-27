from django.views.generic.base import TemplateView


class TableView(TemplateView):
	template_name = 'zabbix_tables/table_index.html'