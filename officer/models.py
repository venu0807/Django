from django.db import models

class Team1(models.Model):
    name=models.CharField(max_length=100)
    fathername=models.CharField(max_length=100)
    age=models.IntegerField()
    batch=models.IntegerField()
    role=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)


class Team2(models.Model):
    name=models.CharField(max_length=100)
    fathername=models.CharField(max_length=100)
    age=models.IntegerField()
    batch=models.IntegerField()
    role=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    