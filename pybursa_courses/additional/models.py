from django.db import models

from courses.models import Course


class Address(models.Model):

    zipcode = models.PositiveIntegerField()
    country = models.CharField(max_length=20)
    region = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    house = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.country + ", " + self.region + ", " + self.street + " " + str(self.house)


class Dossier(models.Model):

    address = models.ForeignKey(Address)
    unliked_courses = models.ManyToManyField(Course, blank=True)
    liked_color = models.CharField(max_length=20)

    def __unicode__(self):
        return str(self.address) + " " + self.liked_color