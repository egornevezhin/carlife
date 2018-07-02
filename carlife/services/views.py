from django.shortcuts import render
from django.http import HttpResponse
from .models import Service
# Create your views here.

def index(request):
    services = Service.objects.order_by('name')
    context = {'services': services}
    return render(request, 'services/services.html', context)