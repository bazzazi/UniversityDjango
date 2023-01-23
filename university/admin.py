from django.contrib import admin
from .models import Content, Course, Student, Registration

# Register your models here.
admin.site.register(Content)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Registration)