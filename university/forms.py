from django.forms import ModelForm
from .models import Student, Course, Content, Registration

class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class CourseForm(ModelForm):
    class Meta:
        model=Course
        fields='__all__'

class ContentForm(ModelForm):
    class Meta:
        model=Content
        fields='__all__'

class RegistrationForm(ModelForm):
    class Meta:
        model=Registration
        fields='__all__'