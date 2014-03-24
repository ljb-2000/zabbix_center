from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages

class TableView(TemplateView):
	template_name = 'zabbix_tables/table_index.html'