from django.db import models

class Pending(models.Model):
    name=models.CharField(max_length=100)
    fathername=models.CharField(max_length=100)
    age=models.IntegerField()
    causeofcomplaint=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)


class Solved(models.Model):
    name=models.CharField(max_length=100)
    fathername=models.CharField(max_length=100)
    age=models.IntegerField()
    causeofcomplaint=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
