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


class UserCourseAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_display_links = ('user',)
    search_fields = ('user',)
    list_filter = ('user',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Student, UserCourseAdmin)
