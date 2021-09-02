from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse('<h1> tech with tim! </h1>')

def v1(response):
    return HttpResponse('<h1> view1 </h1>')

# Create your views here.
