from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import *


class AddLessonForm(forms.Form):
    title = forms.CharField(max_length=255, label="Название", widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=255, label="Описание", widget=forms.TextInput(attrs={'class': 'form-control' }))
    files_url = forms.URLField(label="Ссылка на файлы", widget=forms.URLInput(attrs={'class': 'form-control'}))
    survey_url = forms.URLField(label="Ссылка на форму с д/з", widget=forms.URLInput(attrs={'class': 'form-control'}))
    is_publish = forms.BooleanField(label="Публикация", initial=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    course_id = forms.ModelChoiceField(queryset=Course.objects.all(), label="Курс", empty_label="Выберите", widget=forms.Select(attrs={'class': 'form-select'}))


class EditProfile(forms.Form):
    first_name = forms.CharField(max_length=255, label="Имя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    second_name = forms.CharField(max_length=255, label="Фамилия", widget=forms.TextInput(attrs={'class': 'form-control'}))
    tg_profile = forms.URLField(max_length=255, label="Телеграмм профиль", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=255, label="Почта", widget=forms.TextInput(attrs={'class': 'form-control'}))