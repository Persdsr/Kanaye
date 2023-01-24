from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from oauth.forms import RegisterUserForm, LoginUserForm
from oauth.models import AuthUser
from basic_services.scrap_vk import get_vk


def profile(request, user_slug):
    user = get_object_or_404(AuthUser, username=user_slug)
    context = {}
    if user.vk:
        try:
            user_domain = user.vk.replace('https://vk.com/', '')
            context = {
                'all_vk': get_vk(user_domain)
            }
        except:
            print('Нет подключения')
    return render(request, 'oauth/account.html', context)


class RegisterUserView(CreateView):
    template_name = 'oauth/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        form = RegisterUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            form.save()
            login(self.request, user)
            return redirect('home')
        else:
            return render(request, self.template_name, {'form': form})


class LoginUserView(LoginView):
    template_name = 'oauth/login.html'
    form_class = LoginUserForm

    def get_success_url(self):
        return reverse_lazy('home')


def Logout(request):
    logout(request)
    return redirect('home')