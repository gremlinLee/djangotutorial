from django.contrib import admin
from coaches.models import Coach
from courses.models import Course
from students.models import Student
from additional.models import Dossier, Address


class AdminCourse(admin.ModelAdmin):
    list_display = ('language',
                    'name',
                    'description',
                    'trener',
                    'assistant',
                    'date_of_beginning',
                    'date_of_finishing',
                    'venue')


class AdminStudent(admin.ModelAdmin):
    list_display = ('name',
                    'surname',
                    'date_of_birth',
                    'email',
                    'phone',
                    'package',
                    'dossier')


class AdminCoach(admin.ModelAdmin):
    list_display = ('first_name',
                    'last_name',
                    'course',
                    'role',
                    'user',
                    'dossier'
    )





admin.site.register(Course, AdminCourse)
admin.site.register(Student, AdminStudent)
admin.site.register(Coach, AdminCoach)
admin.site.register(Dossier)
admin.site.register(Address)


