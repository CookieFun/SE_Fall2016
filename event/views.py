# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

from event.models import Column, Event


def index(request):
    columns=Column.objects.all()
    return render(request, 'event/index.html', {'columns':columns})


def column_detail(request, column_slug):
    column=Column.objects.get(slug=column_slug)
    return render(request, 'event/column.html',{'column':column})


def event_detail(request, event_slug):
    event=Event.objects.filter(slug=event_slug)[0]
    return render(request, 'event/event.html',{'event': event})