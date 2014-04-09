# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from api_process.process import *


class ackForm(forms.Form):

    time_select = (
    ('1', 60.0 * 5),
    ('2', 60.0 * 10),
    ('3', 60.0 * 15),
    ('4', 60.0 * 60), 
    ('5', 60.0 * 120),
    ('6', 60.0 * 180),
    ('7', 60.0 * 3600 * 1),
    ('8', 60.0 * 3600 * 7),
    ('9', 60.0 * 3600 * 30),
    )

    ack_text = forms.CharField(help_text='Please input comments')
    time_snoozes = forms.ChoiceField(choices=time_select)
    