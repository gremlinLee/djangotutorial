from django.db import models
from django.contrib.auth.models import User

from additional.models import Dossier


class Coach(models.Model):

    COACH_CHOISE = (
        ('assistant', 'Assistant'),
        ('coach', 'Coach')
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=COACH_CHOISE)
    user = models.ForeignKey(User)
    dossier = models.OneToOneField(Dossier, blank=True)

    def __unicode__(self):
        return self.first_name + " " + self.last_name + "(" + self.role + ")"