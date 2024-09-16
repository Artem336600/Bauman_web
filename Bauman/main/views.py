from django.shortcuts import render



def index(request):
    data = {
        'title': 'Зачем создан данный сайт?',
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def compare(request):
    data = {
        'title': ''
    }
    return render(request, 'main/compare.html')


def caf(request):
    data = {
        'title': ''
    }
    return render(request, 'main/caf.html')
