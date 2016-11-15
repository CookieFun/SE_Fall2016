from django.conf.urls import url

from . import views, addrecord

urlpatterns = [
    url(r'^add-record', addrecord.enter),
    url(r'^post-record', addrecord.receive),
    url(r'static/files', addrecord.upload),
]
