from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'first_django_app/index.html')


def rita(request):
    return HttpResponse("Hello Rita!!")


def girwar(request):
    return HttpResponse("Hello Girwar!!")


def greet(request, name) :
    return HttpResponse(f"Hello {name.capitalize()}!!")