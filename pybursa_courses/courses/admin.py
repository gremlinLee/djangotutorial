from django.contrib import admin
from coaches.models import Coach
from courses.models import Course
from students.models import Student
from additional.models import Dossier, Address

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Coach)
admin.site.register(Dossier)
admin.site.register(Address)
