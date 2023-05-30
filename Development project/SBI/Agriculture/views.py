from django.shortcuts import render
from django.http import HttpResponse
import datetime

def sdatetime(r):
    cdt = datetime.datetime.now()
    return HttpResponse('<h1> Current date time is'+str(cdt)+'</h1>')
