from django.shortcuts import render
from .forms import CheckForm, RegForm
from django.http import HttpResponse
from .models import Order, Status
from django.shortcuts import get_object_or_404, render
import datetime

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = CheckForm(request.POST)
        if form.is_valid():
            try:
                car = Order.objects.get(pk=request.POST.get('id'))
                return render(request, 'check/result.html', {'status': car.status})
            except:
                return render(request, 'check/result.html', {'status': 'не найдено'})
    else:
        form = CheckForm()

    return render(request, 'check/check.html', {'form': form})


def registration(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            o = Order()
            o.name = request.POST.get('name')
            o.phone = request.POST.get('phone')
            o.date = datetime.datetime.strptime(request.POST.get('date'), "%d.%m.%Y").strftime("%Y-%m-%d")
            o.status = Status.objects.get(pk=4)
            o.problem = request.POST.get('problem')
            o.save()
            return render(request, 'check/registration.html', {'status': 'ok', 'id': o.id})
    else:
        form = RegForm()

    return render(request, 'check/registration.html', {'form': form})