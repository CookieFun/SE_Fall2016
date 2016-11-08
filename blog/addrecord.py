from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError
import os
from django.http import HttpResponse,HttpRequest


# Create your views here.


def redirect(request):
    return render(request, 'add record.html')


def handle_context(request):
    if request.method == 'POST':
        print('here')
        print(request)
        print(request.POST['context'])


@csrf_exempt
def receive(request):
    handle_context(request)
    return render(request, 'index.html')


@csrf_exempt
def upload(request):
    print(request.FILES)
    if request.method == 'POST':
        print('file:')
        print(request)
        # if request.FILES is not None:
        #     file = request.FILES[0]
        #     filename = file.filename
        #     print(11)
        #     print(filename)
        return HttpResponse('upload-success')
    else:
        print('empty')
