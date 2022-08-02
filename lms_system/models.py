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
        return f'{self.title} | {str(self.form)} класс'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-form', 'teacher']


class Lesson(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.CharField(max_length=255, verbose_name='Описание')
    files_url = models.URLField(verbose_name='Ссылка на файлы')
    is_publish = models.BooleanField(default=False, verbose_name='Опубликовано?')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    course_id = models.ForeignKey(Course, null=True, on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['-time_create']


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.student.save()
    except ObjectDoesNotExist:
        Student.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.student.save()
