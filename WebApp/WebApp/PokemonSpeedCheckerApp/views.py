from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def speed_checker(request):
    return HttpResponse("Hello")