from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# не забыть про redirect, url_for
from lms_system.forms import *
from lms_system.models import Course


def index(request):
    return render(request, 'lms_system/index.html')


@login_required(login_url='/login')
def profile(request):
    current_user = request.user
    courses = Student.objects.get(pk=current_user.id).course.all()
    context = {
        'title': 'Профиль',
        'courses': courses,
    }
    return render(request, 'lms_system/profile.html', context=context)


# TODO: Добавить айдишник, страница отображает курс с карточками уроков
def course(request, course_id):
    course = Course.objects.get(pk=course_id)
    lessons = Lesson.objects.filter(course_id=course_id).order_by('time_create')
    context = {
        'title': course.title,
        'course': course,
        'lessons': lessons,
    }
    return render(request, 'lms_system/course.html', context=context)


# TODO: Добавить айдишник курса и урока, страница отображает окно трансляции, кнопочки с конспектом и д/з
def lesson(request, course_id, lesson_id):
    context = {
        'title': 'Название урока'
    }
    return render(request, 'lms_system/lesson.html', context=context)


# TODO: страница со всеми курсами, доступно купить и перейти в платёжную систему
def courses(request):
    context = {
        'title': 'Все курсы',
        'courses': Course.objects.all()
    }
    return render(request, 'lms_system/courses.html', context=context)


# TODO: оплата курса, махинации с платёжной системой(ну на всякий случай). Айдишник какой курс купить
def pay_course(request, course_id):
    context = {
        'title': 'Оплата курса'
    }
    current_user = request.user
    course = Course.objects.get(pk=course_id)
    student = Student.objects.get(pk=current_user.id)
    course.student_set.add(student)
    return redirect('profile')


# TODO: красивая формочка, доступна только с ролью учитель
def create_lesson(request):
    if request.method == 'POST':
        form = AddLessonForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Lesson.objects.create(**form.cleaned_data)
                return redirect('cr_lesson')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddLessonForm()
    context = {
        'title': 'Создать урок',
        'form': form
    }
    return render(request, 'lms_system/create_lesson.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('Страница не найдена')


def page_error_view(request, exception=None):
    return HttpResponseNotFound('Ошибка 500')


def permission_denied_view(request, exception=None):
    return HttpResponseNotFound('Отказано в доступе')


def bad_request_view(request, exception=None):
    return HttpResponseNotFound('Некорректный запрос к серверу')
