# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from event.models import Column, Event
from event import form


def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    allevent = column.event_set.all().order_by('-pub_time')
    rightup = Event.objects.all().order_by('-pub_time')[:2]
    return render(request, 'event/column.html', {
        'allevent': allevent,
        'column': column,
        'current': 2,
        'rightup': rightup,
    })


def event_detail(request, id, event_slug):
    at_home = True
    event = Event.objects.get(id=id)
    rightup = Event.objects.all().order_by('-pub_time')[:2]
    if event_slug != event.slug:
        return redirect(event, permanent=True)

    return render(request, 'event/event.html', {
        'event': event,
        'current': 2,
        'rightup': rightup,
    })

def all_events(request):
    allevent = Event.objects.all().order_by('-pub_time')
    print(allevent)
    rightup = Event.objects.all().order_by('-pub_time')[:2]
    return render(request, 'event/column.html', {
        'allevent': allevent,
        'current': 2,
        'rightup': rightup,
    })





