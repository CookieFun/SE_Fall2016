from django.conf.urls import url

from . import views,addrecord

urlpatterns = [
    url(r'^$', views.index, name='index'),
 	url(r'^index$', views.index, name='index'),
    url(r'^add-record', addrecord.redirect),
]