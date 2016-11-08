# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from event.models import Column, Event


def index(request):
    home_display_columns = Column.objects.filter(home_display=True)
    nav_display_columns = Column.objects.filter(nav_display=True)
    return render(request, 'event/index.html', {
        'home_display_columns': home_display_columns,
        'nav_display_columns': nav_display_columns,
        'homepage': True,
    })


def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'event/column.html', {'column': column, 'homepage': False, })


def event_detail(request, id, event_slug):
    at_home = True
    event = Event.objects.get(id=id)
    if event_slug != event.slug:
        return redirect(event, permanent=True)

    return render(request, 'event/event.html', {'event': event,'homepage': False, })
