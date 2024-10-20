from django import forms

class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=30, label='Логин')
    password = forms.CharField(max_length=30, widget=forms.PasswordInput, label='Пароль')
    confirm_password = forms.CharField(max_length=30, widget=forms.PasswordInput, label='Повторите пароль')
    age = forms.IntegerField(label='Возраст', min_value=1)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        age = cleaned_data.get('age')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'Пароли не совпадают')

        if age and age < 18:
            self.add_error('age', 'Вы должны быть старше 18')

        return cleaned_data