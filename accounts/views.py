from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User


class PasswordsChangeView(PasswordChangeView):
    from_class = PasswordChangeForm
    success_url = reverse_lazy('profile')
    template_name = 'change_password.html'


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
