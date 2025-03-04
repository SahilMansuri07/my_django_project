from django.db import models
import datetime

# Create your models here.
class Registeration(models.Model):
    name = models.CharField(max_length=255,default='')
    email = models.EmailField(max_length=255,default='')
    password = models.CharField(max_length=255,default='')
    
class Course(models.Model):
    name = models.CharField(max_length=255,default='')
    description = models.CharField(max_length=255,default='')
    
class Subject(models.Model):
    name = models.CharField(max_length=255,default='')
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    
class Enrollment(models.Model):
    registeration = models.ForeignKey(Registeration,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    enrolled_on = models.DateField(default=datetime.date.today)