from django.db import models



class Course(models.Model):
    language = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    trener = models.ForeignKey('coaches.Coach', related_name='coach')
    assistant = models.ForeignKey('coaches.Coach', related_name='assistant')
    date_of_beginning = models.DateField()
    date_of_finishing = models.DateField()
    venue = models.ForeignKey('additional.Address')

    def __unicode__(self):
        return self.name + "(" + self.name + ")"
