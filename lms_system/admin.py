from django.contrib import admin

from .models import *


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',
                    'form', 'teacher',
                    'cost', 'tg_channel',
                    'is_publish', 'time_create')
    list_display_links = ('title',)
    search_fields = ('title', 'form', 'teacher')
    list_filter = ('teacher', 'form', 'is_publish', 'time_create')


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',
                    'files_url', 'is_publish',
                    'time_create')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('is_publish', 'time_create')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'second_name', 'first_name', 'tg_profile', 'email', 'role')
    list_display_links = ('user', 'first_name', 'second_name', 'tg_profile', 'email', 'role')
    search_fields = ('user', 'first_name', 'second_name', 'tg_profile', 'email', 'role')


class HomeworkTeacherAdmin(admin.ModelAdmin):
    list_display = ('course', 'lesson', 'questions', 'answers', 'deadline', 'time_create')
    list_display_links = ('course', 'lesson')
    search_fields = ('course', 'lesson', 'questions', 'answers', 'deadline', 'time_create')
    list_filter = ('course', 'lesson', 'deadline', 'time_create')


class HomeworkStudentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'lesson', 'answers', 'score', 'time_done')
    list_display_links = ('student', 'course', 'lesson')
    search_fields = ('student', 'course', 'lesson', 'answers', 'score', 'time_done')
    list_filter = ('student', 'course', 'lesson', 'time_done')


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Student, StudentAdmin)
# admin.site.register(HomeworkTeacher, HomeworkTeacherAdmin)
# admin.site.register(HomeworkStudent, HomeworkStudentAdmin)
