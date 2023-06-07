from django.db import models


# Create your models here.
class Student(models.Model):
    roll_number = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    marks = models.IntegerField()
