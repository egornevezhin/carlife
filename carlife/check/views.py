from django.shortcuts import render
from .forms import CheckForm
from django.http import HttpResponse
from .models import Order
from django.shortcuts import get_object_or_404, render

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
