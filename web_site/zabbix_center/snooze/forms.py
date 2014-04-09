# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from api_process.process import *


class ackForm(forms.Form):

    time_select = (
    (20 * 1,   '20 seconds'),
    (60 * 5,   '5 min'),
    (60 * 10,  '10 min'),
    (60 * 15,  '15 min'),
    (60 * 60,  '1 hour'), 
    (60 * 120, '2 hours'),
    (60 * 180, '3 hours'),
    (60 * 3600 * 1, '1 day'),
    (60 * 3600 * 7, '7 days'),
    (60 * 3600 * 30, '30 days'),
    )

    ack_text = forms.CharField(help_text='Please input comments')
    time_snoozes = forms.ChoiceField(choices=time_select)
    