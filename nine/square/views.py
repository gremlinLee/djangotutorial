from django.shortcuts import render
from math import sqrt


def index(request):
    print request.GET
    answer = {}
    mapget = request.GET

    if len(mapget.keys()) == 3:
        answer = quad(mapget)

    return render(request, "square/index.html", answer)


def quad(mapget):
    try:
        answer = {
            'answer': {
                'allisrigth': {},
                'error': ""
            }
        }
        a = int(mapget.get('a'))
        b = int(mapget.get('b'))
        c = int(mapget.get('c'))
        d = b * b - 4 * a * c
        print answer
        d = sqrt(d)
        x1 = (-b + d) / (2 * a)
        x2 = (-b - d) / (2 * a)
        print x1, x2
        answer.get('answer')['allisright'] = {}
        answer.get('answer')['allisright']['x1'] = x1
        answer.get('answer')['allisright']['x2'] = x2

    except ValueError as error:
        answer.get('answer')['error'] = "Error " + str(error) + ". D is negative, please enter correct data."
        print error

    return answer
