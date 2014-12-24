from django.shortcuts import render
from django.shortcuts import redirect
from django.views import generic
from django.views.generic.edit import CreateView
from django import forms

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


class StudentForm(forms.Form):
    PACKAGE_CHOICES = (
        ('standart', 'Standart'),
        ('gold', 'Gold'),
        ('vip', 'VIP'),
    )
    student_name = forms.CharField(max_length=100)
    student_package = forms.ChoiceField(
        choices=PACKAGE_CHOICES,
        widget=forms.RadioSelect)
    student_note = forms.CharField(widget=forms.Textarea)


def student_save(request):
    if request.method is 'post':
        form = StudentForm(request.POST)
        if form.is_valid():
            print form.cleaned_data
            return redirect('student_list')
        else:
            form = StudentForm()

        return render(request, 'students/new_student.html', {'form': form})


def student_add(request):
    form = StudentForm()
    return render(request, 'students/new_student.html', {'form': form})


def concrete_student(request, student_id):
    student = Student.objects.get(id=int(student_id))
    print student
    print student_id
    return render(request, "students/student.html", {
        'student': student
    })


class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'surname', 'date_of_birth', 'email', 'courses', 'phone', 'package', 'dossier']
    template_name_suffix = '_create_form'