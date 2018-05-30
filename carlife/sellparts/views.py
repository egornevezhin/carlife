from django.shortcuts import render
from django.http import HttpResponse

from .models import Part
# Create your views here.


def index(request):
    parts = Part.objects.order_by('cost')[:5]
    context = {'parts': parts}
    return render(request, 'sellparts/sellparts.html', context)