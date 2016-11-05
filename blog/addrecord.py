from django.shortcuts import render

# Create your views here.


def redirect(request):
    return render(request, 'add record.html')

