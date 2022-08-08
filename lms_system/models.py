from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Добавление: name_model.objects.create(params)
# Удаление: entry.delete()
# Изменение: entry.update(field='some value')
# Все записи: name_model.objects.all(params)
# Фильтр(соответствующие критерию записи): name_model.objects.filter(cond)
# Фильтр(все не соответствующие критерию записи): name_model.objects.filter(cond)
# Фильтр(все не соответствующие критерию записи): name_model.objects.filter(cond)
# Взятие записи с генерацией исключения: name_model.objects.get(cond)
# Сортировка: name_model.objects.order_by(field)
STATUS_CHOICES = (
    ('t', 'Учитель'),
    ('s', 'Ученик'),
    ('a', 'Администратор'),
)


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.CharField(max_length=255, verbose_name='Описание')
    form = models.IntegerField(verbose_name="Класс")
    # подумать над отношением с айдишником юзера а не простым текстом
    teacher = models.CharField(max_length=255, verbose_name='Учитель')
    cost = models.IntegerField(verbose_name='Стоимость')
    tg_channel = models.URLField(verbose_name='Телеграмм канал')
    is_publish = models.BooleanField(default=False, verbose_name='Опубликован?')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-form', 'teacher']


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    second_name = models.CharField(max_length=255, verbose_name='Фамилия')
    tg_profile = models.URLField(verbose_name='Ссылка на Телаграмм')
    email = models.EmailField(verbose_name='Почта')
    course = models.ManyToManyField(Course, verbose_name='Курс', null=True, blank=True)
    role = models.CharField(max_length=255, choices=STATUS_CHOICES, default='s', verbose_name='Роль')

    def __str__(self):
        return f'{self.first_name} {self.second_name}'

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
        ordering = ['first_name', 'second_name']


class Lesson(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.CharField(max_length=255, verbose_name='Описание')
    files_url = models.URLField(verbose_name='Ссылка на файлы')
    survey_url = models.URLField(verbose_name='Ссылка на форму с д/з')
    is_publish = models.BooleanField(default=False, verbose_name='Опубликовано?')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    course_id = models.ForeignKey(Course, null=True, on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['-time_create']


# class HomeworkTeacher(models.Model):
#     course = models.OneToOneField(Course, on_delete=models.CASCADE, verbose_name='Название курса')
#     lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, verbose_name='Название урока')
#     questions = models.FileField(verbose_name='Вопросы')
#     answers = models.TextField(verbose_name='Ответы')
#     deadline = models.DateTimeField(verbose_name='Дедлайн')
#     time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
#
#     def __str__(self):
#         return f'{self.lesson} домашнее задание'
#
#     class Meta:
#         verbose_name = 'Домашнее задание(учителям)'
#         verbose_name_plural = 'Домашние задания(учителям)'
#         ordering = ['course', 'time_create']


# class HomeworkStudent(models.Model):
#     student = models.OneToOneField(Student, on_delete=models.CASCADE, verbose_name='Ученик')
#     course = models.OneToOneField(Course, on_delete=models.CASCADE, verbose_name='Название курса')
#     lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, verbose_name='Название урока')
#     answers = models.FileField(verbose_name='Ответы')
#     score = models.IntegerField(verbose_name='Балл')
#     time_done = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
#
#     def __str__(self):
#         return f'{self.lesson} домашнее задание'
#
#     class Meta:
#         verbose_name = 'Домашнее задание(ученикам)'
#         verbose_name_plural = 'Домашние задания(ученикам)'
#         ordering = ['course', 'time_done']


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.student.save()
    except ObjectDoesNotExist:
        Student.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.student.save()
