from django.shortcuts import render
from django.views import generic

from students.models import Student


class StudentListView(generic.ListView):
    template_name = 'students/students.html'
    context_object_name = 'student_list'

    def get_queryset(self):
        print Student.objects.all()[:1]
        student = Student.objects.all()[0]
        print student.name
        print student.surname
        return Student.objects.order_by('-name')


def concrete_student(request, student_id):
    student = Student.objects.get(id=int(student_id))
    print student
    print student_id
    return render(request, "students/student.html", {
        'student': student
    })