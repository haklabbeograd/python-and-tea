from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    return HttpResponse('Hello from Python!')


def add(request):

    temp = Temperature()
    temp.value = 11.2
    temp.save()
    
    return HttpResponse('OK')

def get(request):

    temps = Temperature.objects.all()

    return render(request, 'temps.html', {'temps': temps})

