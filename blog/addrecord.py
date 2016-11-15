from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from event.models import Column, Event

from blog.models import UploadFile
from blog.forms import UploadFileForms


def enter(request):
    return render(request, 'add_record.html', {
        'current': 3,
    })


def handle_context(request):
    if request.method == 'POST':
        print('here')
        print(request)
        print(request.POST['context'])
        print(request.POST['title'], request.POST['date'],
              request.POST['place'], request.POST['people'])
        Event.objects.get_or_create(
            title=request.POST['title'],
            event_time = request.POST['date'],
            place=request.POST['place'],
            speaker=request.POST['people'],
            slug='event',
            content=request.POST['context']
        )


@csrf_exempt
def receive(request):
    print("receive")
    handle_context(request)
    return HttpResponse('<script>alert(\'Add-record successful\');window.location.href="../"; </script>')


@csrf_exempt
def upload(request):
    print(request.FILES)
    if request.method == 'POST':
        print('file:')
        print(request)
        print('trying to save')
        newfile = UploadFile(upload_file=request.FILES['uploadFileName'])
        newfile.save()
        # if request.FILES is not None:
        #     file = request.FILES.get('uploadFileName')
        #     print('trying to save into disk...', file.name)
        #     path = default_storage.save('tmp/'+file.name, ContentFile(file.read()))
        #     tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        return HttpResponse('tmp_file')
    else:
        form = UploadFileForms()
        print('empty')
        return HttpResponse('upload-fail')
