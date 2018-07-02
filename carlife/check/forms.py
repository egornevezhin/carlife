from django import forms
from django.utils import timezone


class CheckForm(forms.Form):
    id = forms.CharField(label='Номер заказа', max_length=15)
    # car_number = forms.CharField(label='Номер машины (в формате T001YP178)', max_length=9)


class RegForm(forms.Form):
    name = forms.CharField(max_length=40, label='ФИО заказчика')
    phone = forms.CharField(max_length=12, label='Телефон')
    date = forms.DateField(label='Дата', initial=timezone.now)
    problem = forms.CharField(widget=forms.Textarea, label='Проблема')
