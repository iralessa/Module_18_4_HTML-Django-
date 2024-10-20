"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task2.views import func_view, ClassView
from task4.views import index, shop, cart
from task5.views import registration_page, sign_up_by_django, sign_up_by_html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Главная страница
    path('shop/', shop, name='shop'),  # Магазин
    path('cart/', cart, name='cart'),  # Корзина
    path('register/', registration_page, name='registration'),  # Форма регистрации
    path('html_sign_up/', sign_up_by_html, name='sign_up_by_html'),  # Регистрация через HTML
    path('django_sign_up/', sign_up_by_django, name='sign_up_by_django'),  # Регистрация через Django-форму
]


# Представление для страницы Магазина
# def shop(request):
#     # Словарь с пунктами списка
#     item1 = 'Игровая консоль'
#     item2 = 'гровой контроллер'
#     item3 = 'Игровая гарнитура'
#
#     # Передаём словарь в шаблон через параметр context
#     context = {
#         'item1': item1,
#         'item2': item2,
#         'item3': item3
#     }
#     return render(request, 'third_task/page1.html', context)