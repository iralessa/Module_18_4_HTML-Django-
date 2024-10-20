# views.py в приложении task5
from django.shortcuts import render
from .forms import UserRegisterForm

# Псевдо-список существующих пользователей
users = ['user1', 'user2', 'user3']

def registration_page(request):
    return render(request, 'fifth_task/registration_page.html')

def sign_up_by_django(request):
    # Информация для передачи в шаблон
    info = {}

    # Обработка POST-запроса
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            age = form.cleaned_data['age']

            # Проверка на существование пользователя
            if username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                # Добавляем нового пользователя
                users.append(username)
                return render(request, 'fifth_task/success.html', {'message': f'Приветствуем, {username}!'})

        # Если форма не прошла валидацию, ошибки автоматически добавляются в форму
        info['form'] = form

    else:
        # Если GET-запрос — просто показываем пустую форму
        info['form'] = UserRegisterForm()

    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_html(request):
    # Информация для передачи в шаблон
    info = {}

    # Обработка POST-запроса
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        age = int(request.POST.get('age', 0))

        # Проверка на совпадение паролей
        if password != confirm_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18 лет'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            # Добавляем нового пользователя
            users.append(username)
            return render(request, 'fifth_task/success.html', {'message': f'Приветствуем, {username}!'})

    return render(request, 'fifth_task/registration_page.html', info)
