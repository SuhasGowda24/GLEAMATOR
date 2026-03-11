from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)