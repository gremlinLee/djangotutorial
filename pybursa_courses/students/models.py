from django.db import models
from django.core.urlresolvers import reverse

from courses.models import Course
from additional.models import Dossier


class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    courses = models.ManyToManyField(Course)
    phone = models.CharField(max_length=15)
    package = models.CharField(max_length=15)
    dossier = models.OneToOneField(Dossier)

    def get_absolute_url(self):
        return reverse('students/', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.name + " " + self.surname