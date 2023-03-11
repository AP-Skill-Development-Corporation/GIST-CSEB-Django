from django.db import models

# Create your models here.
class Student(models.Model):
	rno = models.CharField(max_length=20)
	nme = models.CharField(max_length=120)
	em = models.EmailField(max_length=150)
	age = models.IntegerField()
