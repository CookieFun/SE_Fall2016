"""HITIntEvents URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# -*- coding:UTF-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from event import views
from django.conf.urls.static import static
from DjangoUeditor import urls as DjangoUeditor_urls



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^', include('blog.urls')),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),
    # url(r'^$', views.index, name='index'),
    url(r'^column/(?P<column_slug>[^/]+)/$',views.column_detail, name='column'),
    url(r'^event/(?P<id>\d+)/(?P<event_slug>[^/]+)/$',views.event_detail, name='event'),
    url(r'^allevents/', views.all_events, name='allevents'),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    #url(r'^admin/', include(admin.site.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
