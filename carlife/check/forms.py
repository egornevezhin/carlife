from django import forms
from datetime import datetime, timedelta


class CheckForm(forms.Form):

    id = forms.CharField(label='Номер заказа', max_length=15)
    car_number = forms.CharField(label='Номер машины (в формате T001YP178)', max_length=9)
