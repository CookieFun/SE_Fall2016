from django.conf.urls import url

from . import views, addrecord

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^add-record', addrecord.redirect),
    url(r'^post-record', addrecord.receive),
    url(r'static/files', addrecord.upload),
]
