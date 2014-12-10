from django.shortcuts import render
from django.views import generic

from coaches.models import Coach


class CoachListView(generic.ListView):
    template_name = 'coaches/coaches.html'
    context_object_name = 'coach_list'

    def get_queryset(self):
        return Coach.objects.order_by('-first_name')


class ConcreteCoach(generic.DetailView):
    model = Coach
    template_name = 'coaches/coach.html'

#
# def concrete_coach(request, coach_id):
#     coach = Coach.objects.get(id=int(coach_id))
#     print coach.lector, type(coach.lector)
#     return render(request, "coaches/coach.html", {
#         'coach': coach
#     })