
from django.shortcuts import render

def index(request):
    return render(request, 'third_task/index.html')

def shop(request):
    items = {
        'item1': 'Игровая консоль',
        'item2': 'Игровой контроллер',
        'item3': 'Игровая гарнитура'
    }
    return render(request, 'third_task/page1.html', {'items': items})

def cart(request):
    return render(request, 'third_task/page2.html')
