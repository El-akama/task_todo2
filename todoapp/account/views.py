from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls.base import reverse_lazy
from django.views.generic import CreateView

from .forms import RegistrationForm, UserLoginForm


class RegisterView(CreateView):
    model = get_user_model()
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('log-in')


class SigninView(LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('index')

