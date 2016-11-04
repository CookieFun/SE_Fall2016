# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(u'welcome')


def column_detail(request, column_slug):
    return HttpResponse('column slug: ' + column_slug)


def event_detail(request, event_slug):
    return HttpResponse('event slug: ' + event_slug)