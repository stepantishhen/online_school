from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import *


class AddLessonForm(forms.Form):
    title = forms.CharField(max_length=255, label="Название", widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=255, label="Описание", widget=forms.TextInput(attrs={'class': 'form-control' }))
    translation_url = forms.URLField(label="Ссылка на файлы", widget=forms.URLInput(attrs={'class': 'form-control'}))
    is_publish = forms.BooleanField(label="Публикация", initial=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    course_id = forms.ModelChoiceField(queryset=Course.objects.all(), label="Курс", empty_label="Выберите", widget=forms.Select(attrs={'class': 'form-select'}))


class PrettyAuthenticationForm(AuthenticationForm):
    class Meta:
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-class'})
        }