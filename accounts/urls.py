from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('password_edit/', auth_views.PasswordChangeView.as_view(template_name='change_password.html'), name='password_edit')
    path('password_edit/', PasswordsChangeView.as_view(), name='password_edit'),
    path('personal_data/', TemplateView.as_view(template_name="personal_data.html"), name='personal_data'),
    path('user_agreement/', TemplateView.as_view(template_name="user_agreement.html"), name='user_agreement'),
]