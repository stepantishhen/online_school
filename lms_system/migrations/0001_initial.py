# Generated by Django 4.0.5 on 2022-08-08 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('form', models.IntegerField(verbose_name='Класс')),
                ('teacher', models.CharField(max_length=255, verbose_name='Учитель')),
                ('cost', models.IntegerField(verbose_name='Стоимость')),
                ('tg_channel', models.URLField(verbose_name='Телеграмм канал')),
                ('is_publish', models.BooleanField(default=False, verbose_name='Опубликован?')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
                'ordering': ['-form', 'teacher'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('tg_profile', models.URLField(verbose_name='Ссылка на Телаграмм')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('role', models.CharField(choices=[('t', 'Учитель'), ('s', 'Ученик'), ('a', 'Администратор')], default='s', max_length=255, verbose_name='Роль')),
                ('course', models.ManyToManyField(blank=True, null=True, to='lms_system.course', verbose_name='Курс')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Ученик',
                'verbose_name_plural': 'Ученики',
                'ordering': ['first_name', 'second_name'],
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('files_url', models.URLField(verbose_name='Ссылка на файлы')),
                ('survey_url', models.URLField(verbose_name='Ссылка на форму с д/з')),
                ('is_publish', models.BooleanField(default=False, verbose_name='Опубликовано?')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('course_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lms_system.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
                'ordering': ['-time_create'],
            },
        ),
    ]
