from django.http import HttpResponse
from django.shortcuts import render

def home(self):
    return HttpResponse("hello world")