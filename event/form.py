from django import forms
from event.models import Column, Event


class EventModelForm(forms.ModelForm):
    class Meta:
        model=Event
        exclude=()
