from django.shortcuts import render


def index(request):
    context = {
        'title': 'Genealogical Tree Web App',
        'values': ['val1', 'val2', 'val3'],
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')
