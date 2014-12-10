from django.shortcuts import render
from datetime import datetime
from csv import DictReader


class Storage(object):
    def __init__(self, list):
        self.storage = list

    def get_storage(self):
        return self.storage

storage = ""


class Hero(object):
    def __init__(self, surName, firstName, birth_date, nickname=None):
        self.surname = surName
        self.first_name = firstName
        self.birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()
        if nickname is not None:
            self.nickname = nickname

    def __str__(self):
        return "Full name: " + self.first_name + " " + self.surname

    def get_age(self):
        return str(int((
            (datetime.now() - datetime(self.birth_date.year,
                                       self.birth_date.month,
                                       self.birth_date.day)).days / 365.0)))

    def get_fullname(self):
        return self.surname + ' ' + self.first_name


def index(request):
    global storage
    with open('./heroes/data.csv', 'r+') as f:
        reader = DictReader(f,
                            ['id', 'surname',
                             'name', 'birthdate',
                             'nickname'])
        reader.next()
        list_of_heroes = []
        for row in reader:
            p = Hero(
                row['surname'],
                row['name'],
                row['birthdate'],
                row['nickname']
            )
            list_of_heroes.append(p)

        storage = Storage(list_of_heroes)
        print storage
        print list_of_heroes

    return render(request, "heroes/index.html", {'heroes': list_of_heroes})


def detail(request, hero):
    global storage
    print storage
    heroes = storage.get_storage()
    heroobj = ""
    for i in range(0, len(heroes)):
        if hero == heroes[i].nickname:
            heroobj = heroes[i]

    print heroobj
    return render(request, "heroes/detail.html", {
        'hero': heroobj
    })
