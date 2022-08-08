from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('password_edit/', auth_views.PasswordChangeView.as_view(template_name='change_password.html'), name='password_edit')
    path('password_edit/', PasswordsChangeView.as_view(), name='password_edit'),
]