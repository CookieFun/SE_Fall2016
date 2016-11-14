from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'current': 1,
    })

def right(request):
    return render(request, 'right-sidebar.html')