from django.db import models
import uuid

# Create your models here.
class Student(models.Model):
    id=models.UUIDField(unique=True, primary_key=True,editable=False,default=uuid.uuid4)
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    id=models.UUIDField(unique=True, primary_key=True,editable=False,default=uuid.uuid4)
    name=models.CharField(max_length=200)
    content=models.ManyToManyField('Content',blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Registration(models.Model):
    id=models.UUIDField(unique=True, primary_key=True,editable=False,default=uuid.uuid4)
    Course_ID=models.ForeignKey('Course', on_delete=models.CASCADE)
    Student_ID=models.ForeignKey('Student',on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Course_ID.name+" "+self.Student_ID.name

class Content(models.Model):
    id=models.UUIDField(unique=True, primary_key=True,editable=False,default=uuid.uuid4)
    des=models.CharField(max_length=500)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.des




