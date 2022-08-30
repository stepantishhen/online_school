from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import uuid

from yookassa import Payment, Configuration

# не забыть про redirect, url_for
from lms_system.forms import *
from lms_system.models import Course


def index(request):
    return render(request, 'lms_system/index.html', context={'courses': Course.objects.all()})


@login_required(login_url='/accounts/login')
def profile(request):
    current_user = request.user
    courses = Student.objects.get(pk=current_user.id).course.all()
    context = {
        'title': 'Профиль',
        'courses': courses,
        'student': Student.objects.get(pk=current_user.id),
    }
    return render(request, 'lms_system/profile.html', context=context)


@login_required(login_url='/accounts/login/')
def course(request, course_id):
    course = Course.objects.get(pk=course_id)
    lessons = Lesson.objects.filter(course_id=course_id).order_by('time_create')
    print(lessons)
    context = {
        'course': course,
        'lessons': lessons,
        # 'homeworks': HomeworkTeacher.objects.filter(course=course_id)
    }
    return render(request, 'lms_system/course.html', context=context)


@login_required(login_url='/accounts/login/')
def courses(request):
    context = {
        'title': 'Все курсы',
        'courses': Course.objects.all()
    }
    return render(request, 'lms_system/courses.html', context=context)


@login_required(login_url='/accounts/login/')
def pay_course(request, course_id):
    context = {
        'title': 'Оплата курса'
    }
    current_user = request.user
    course = Course.objects.get(pk=course_id)
    student = Student.objects.get(pk=current_user.id)

    Configuration.account_id = 932158
    Configuration.secret_key = 'test_PXTbJODJWZ60YN6KlyGGeQagvvwDDbEnxYOyszMXZI8'

    pay_id = uuid.uuid4()
    payment = Payment.create({
        "amount": {
            "value": f"{course.cost}.00",
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": f"http://127.0.0.1:8000/success/{pay_id}/{course_id}",
            # "return_url": "https://www.merchant-website.com/return_url",
        },
        "capture": True,
        "description": f"Оплата курса {course.title}"
    }, pay_id)
    confirmation_url = payment.confirmation.confirmation_url
    return redirect(confirmation_url)


@login_required(login_url='/accounts/login/')
def success(request, idempotence_key, course_id):
    Configuration.account_id = 932158
    Configuration.secret_key = 'test_PXTbJODJWZ60YN6KlyGGeQagvvwDDbEnxYOyszMXZI8'
    payment = Payment.find_one(idempotence_key)
    return HttpResponse(f"{payment.status}")


@login_required(login_url='/accounts/login/')
def create_lesson(request):
    current_user = request.user
    if request.method == 'POST':
        form = AddLessonForm(request.POST)
        if form.is_valid():
            Lesson.objects.create(**form.cleaned_data)
            return redirect('cr_lesson')
    else:
        form = AddLessonForm()
    return render(request, 'lms_system/form.html', {'form': form, 'title': 'Создать урок',
                                                    'button': 'Создать',
                                                    'student': Student.objects.get(pk=current_user.id)})


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    if request.method == "POST":
        form = EditProfile(request.POST)
        if form.is_valid():
            edited = Student.objects.filter(pk=request.user.id)
            edited.update(
                first_name=request.POST.get('first_name'),
                second_name=request.POST.get('second_name'),
                tg_profile=request.POST.get('tg_profile'),
                email=request.POST.get('email')
            )
    else:
        form = EditProfile()
    student = Student.objects.filter(pk=request.user.id)[0]
    form = EditProfile(initial={'first_name': student.first_name,
                                'second_name': student.second_name,
                                'tg_profile': student.tg_profile,
                                'email': student.email})
    return render(request, 'lms_system/form.html', {'form': form, 'title': 'Изменить профиль',
                                                    'button': 'Изменить',
                                                    'student': Student.objects.get(pk=current_user.id)})


# @login_required(login_url='/accounts/login/')
# def homeworks(request):
#     current_user = request.user
#     current_student = Student.objects.get(pk=current_user.id)
#     context = {
#         'title': 'Домашние задания',
#         'student': current_student,
#         'homeworks': HomeworkTeacher.objects.filter(course__in=current_student.course.all())
#     }
#     return render(request, 'lms_system/homeworks.html', context=context)


# @login_required(login_url='/accounts/login/')
# def homeworks(request, homework_id):
#     context = {}
#     return render(request, 'lms_system/homework.html', context=context)


def page_not_found(request, exception):
    return render(request, 'lms_system/error.html', context={'error': 'Страница не найдена'})


def page_error_view(request, exception=None):
    return render(request, 'lms_system/error.html', context={'error': 'Ошибка 500'})


def permission_denied_view(request, exception=None):
    return render(request, 'lms_system/error.html', context={'error': 'Отказано в доступе'})


def bad_request_view(request, exception=None):
    return render(request, 'lms_system/error.html', context={'error': 'Некорректный запрос к серверу'})
