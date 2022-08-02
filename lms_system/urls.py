from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('profile/', profile, name='profile'),
    path('courses/', courses, name='courses'),
    path('course/<int:course_id>/', course, name='crs_page'),
    # path('course/<int:course_id>/lesson/<int:lesson_id>/', lesson, name='lessom'),
    path('create_lesson/', create_lesson, name='cr_lesson'),
    path('pay/<int:course_id>/', pay_course, name='pay'),
]