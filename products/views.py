from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse




def hello(request):
    if request.method == 'GET':
        return HttpResponse('hello its my first project')


def now_time(request):
    if request.method == 'GET':
        now_time = datetime.now()
        return HttpResponse(now_time)

def goodby(request):
    if request.method == 'GET':
        return HttpResponse('Good bye BRO')

