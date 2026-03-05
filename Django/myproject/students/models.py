from django.db import models

# Create your models here.
class students(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    
    def __str__(self):
        return self.name
    
class course(models.Model):
    title=models.CharField(max_length=100)
    students=models.ForeignKey(students,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    