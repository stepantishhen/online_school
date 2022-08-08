from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('profile/', profile, name='profile'),
    path('courses/', courses, name='courses'),
    path('course/<int:course_id>/', course, name='crs_page'),
    path('create_lesson/', create_lesson, name='cr_lesson'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('pay/<int:course_id>/', pay_course, name='pay'),
    path('success/<str:pay_id>/<int:course_id>', success, name='success'),
    # path('homeworks/', homeworks, name='homeworks'),
    # path('homework/<int:homework_id>', homeworks, name='homework'),
]