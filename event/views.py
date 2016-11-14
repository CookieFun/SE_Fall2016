# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from event.models import Column, Event
from event import form


def index(request):
    home_display_columns = Column.objects.filter(home_display=True)
    nav_display_columns = Column.objects.filter(nav_display=True)
    return render(request, 'event/index.html', {
        'home_display_columns': home_display_columns,
        'nav_display_columns': nav_display_columns,
        'nav_show': 'home',
    })


def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'event/column.html', {'column': column, 'nav_show': column.name, })


def event_detail(request, id, event_slug):
    at_home = True
    event = Event.objects.get(id=id)
    print(event.content)
    if event_slug != event.slug:
        return redirect(event, permanent=True)

    return render(request, 'event/event.html', {'event': event, 'nav_show': event.column.all()[0].name})


def add_event(request):
    if request.method == 'POST':
        print("!")
        name = request.GET['name']
        content = request.GET['content']
        return HttpResponse(content)
    else:
        print("-")
        return render(request, 'event/add_record.html', )

