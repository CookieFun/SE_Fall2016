from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings


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
        if request.FILES is not None:
            file = request.FILES.get('uploadFileName')
            print('trying to save into disk...', file.name)
            path = default_storage.save('tmp/'+file.name, ContentFile(file.read()))
            tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        return HttpResponse('tmp_file')
    else:
        print('empty')
        return HttpResponse('upload-fail')

