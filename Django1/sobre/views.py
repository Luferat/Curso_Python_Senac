from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def metodoSobre (request):
    return HttpResponse('Esta é a sobre!')

