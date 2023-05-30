from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def show(r):
    return HttpResponse('<h1>H Hi from django server</h1>')

def display(r):
    return HttpResponse('<h1> welcome to 1st session of Django')

def m1(r):
    return HttpResponse('<h1> showing M1 Application</h1>')