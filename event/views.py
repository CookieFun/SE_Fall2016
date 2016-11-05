# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

from event.models import Column, Event


def index(request):
    columns=Column.objects.all()
    return render(request, 'index.html', {'columns':columns})


def column_detail(request, column_slug):
    column=Column.objects.get(slug=column_slug)
    #return HttpResponse('column slug: ' + column_slug)
    return render(request, 'event/column.html',{'column':column})


def event_detail(request, event_slug):
    #return HttpResponse('event slug: ' + event_slug)
    event=Event.objects.get(slug=event_slug)
    return render(request, 'event/event.html',{'event': event})