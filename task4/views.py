from django.shortcuts import render

# Представление для главной страницы
# def index(request):
#     text = 1111
#     list = [1.1, 2.2,3.3]
#     len_list = len(list)
#     name = 'IRA'
#     context = {
#         'list': list,
#         'text': text,
#         'name': name,
#         'len_list': len_list
#     }
#     return render(request, 'fourth_task/index.html',context)
def index(request):
    return render(request, 'fourth_task/index.html')


# Представление для магазина
# def shop(request):
#     games = {'games': ['Atomic Heart', 'Cyberpunk 2077']}
#     return render(request, 'fourth_task/page1.html', games)

def shop(request):
    games = ['Atomic Heart', 'Cyberpunk 2077']
    context = {
        'games': games,
    }
    return render(request, 'fourth_task/page1.html', context)

# Представление для корзины
def cart(request):
    return render(request, 'fourth_task/page2.html')
