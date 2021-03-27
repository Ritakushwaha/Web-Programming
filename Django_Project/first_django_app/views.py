from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Hello!!")


def rita(request):
    return HttpResponse("Hello Rita!!")


def girwar(request):
    return HttpResponse("Hello Girwar!!")