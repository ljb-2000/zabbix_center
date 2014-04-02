# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from api_process.process import *




class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    email = forms.EmailField(required=False)
    cc_myself = forms.BooleanField(required=False)
    

class addHostsForm(forms.Form):

    templates = Spider().template_list()
    groups = process_base().gid_2_group_list()

    template_choices = [(item['templateid'], item['name']) for item in templates]
    group_choices = [(item['groupid'], item['name']) for item in groups]

    hosts = forms.CharField(help_text='Please input the host ip you need to add. Multiple ip you should use space to split like "1.2.3.4 1.2.3.4 1.2.3.4"')
    templateids = forms.MultipleChoiceField(
        choices=template_choices, 
        help_text='Check what template as you want to add to hosts',
        widget=forms.CheckboxSelectMultiple)
    group = forms.ChoiceField(choices=group_choices)
    

    
