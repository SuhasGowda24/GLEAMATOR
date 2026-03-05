from django.contrib import admin
from  .models import students
from  .models import course

admin.site.register(students)
admin.site.register(course)