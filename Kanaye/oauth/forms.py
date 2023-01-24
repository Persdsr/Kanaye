from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from oauth.models import AuthUser


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Логин', }))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', }))


class RegisterUserForm(UserCreationForm):
    """Форма регистраций"""
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Логин', }))
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'class': 'forms__userMail input-default', 'placeholder': 'Почта'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'forms__userName input-default', 'placeholder': 'Имя'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'forms__userName input-default', 'placeholder': 'Фамилия'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'forms__userPass input-default', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'forms__userPass input-default', 'placeholder': 'Повтор пароля'}))

    field_order = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    class Meta:
        model = AuthUser
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
