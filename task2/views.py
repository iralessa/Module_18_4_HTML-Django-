from django.shortcuts import render
from django.views.generic import TemplateView

# Функция для функционального представления
def func_view(request):
    return render(request, 'second_task/func_template.html')

# Классовое представление
class ClassView(TemplateView):
    template_name = 'second_task/class_template.html'