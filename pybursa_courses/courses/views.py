from django.shortcuts import render
from django.views import generic

from courses.models import Course


class CourseListView(generic.ListView):
    template_name = 'courses/courses.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        return Course.objects.order_by('-name')


def concrete_course(request, course_id):
    course = Course.objects.get(id=int(course_id))
    print course
    return render(request, "courses/course.html", {
        'course': course
    })