from django.shortcuts import render
from .forms import *

# Create your views here.

# index Page
def index(request):
    return render(request, 'university/index.html')

# Student
def add_student(request):
    forms=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()

    context={
        'form':forms
    }
    return render(request, 'university/add_student.html',context=context)
def remove_student(request,pk):
    student=Student.objects.get(id=pk)
    if request.method=='POST':
        student.delete()
    context={
        'content':student
    }
    return render(request, 'university/remove_student.html',context=context)
def edit_student(request,pk):
    student=Student.objects.get(id=pk)
    forms=StudentForm(instance=student)
    if request.method=='POST':
        form=StudentForm(request.method, instance=student)
        if form.is_valid():
            form.save()
    context={
        'form':forms
    }
    return render(request, 'university/edit_student.html',context=context)
def read_student(request):
    return render(request, 'university/read_student.html')

# Content
def add_content(request):
    forms=ContentForm()
    if request.method=='POST':
        form=ContentForm(request.POST)
        if form.is_valid():
            form.save()
            
    context={
        'form':forms
    }
    return render(request, 'university/add_content.html', context=context)
def remove_content(request, pk):
    content=Content.objects.get(id=pk)
    if request.method=='POST':
        content.delete()
    context={
        'content':content
    }
    return render(request, 'university/remove_content.html', context=context)
def edit_content(request,pk):
    content=Content.objects.get(id=pk)
    forms=ContentForm(instance=content)
    if request.method=='POST':
        form=ContentForm(request.method, instance=content)
        if form.is_valid():
            form.save()
    context={
        'form':forms
    }
    return render(request, 'university/edit_content.html',context=context)
def read_content(request, pk):
    return render(request, 'university/read_content.html')

# Course
def add_course(request):
    forms=CourseForm()
    if request.method=='POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            
    context={
        'form':forms
    }
    return render(request, 'university/add_course.html',context=context)
def remove_course(request,pk):
    course=Course.objects.get(id=pk)
    if request.method=='POST':
        course.delete()
    context={
        'course':course
    }
    return render(request, 'university/remove_course.html',context=context)
def edit_course(request,pk):
    course=Student.objects.get(id=pk)
    forms=Course(instance=course)
    if request.method=='POST':
        form=Course(request.method, instance=course)
        if form.is_valid():
            form.save()
    context={
        'form':forms
    }
    return render(request, 'university/edit_course.html',context=context)
def read_course(request, pk):
    return render(request, 'university/read_course.html')

# Registration
def add_registration(request):
    forms=RegistrationForm()
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            
    context={
        'form':forms
    }
    return render(request, 'university/add_registration.html',context=context)
def remove_registration(request,pk):
    registration=Registration.objects.get(id=pk)
    if request.method=='POST':
        registration.delete()
    context={
        'registration':registration
    }
    return render(request, 'university/remove_registration.html',context=context)
def edit_registration(request,pk):
    registration=Student.objects.get(id=pk)
    forms=RegistrationForm(instance=registration)
    if request.method=='POST':
        form=RegistrationForm(request.method, instance=registration)
        if form.is_valid():
            form.save()
    context={
        'form':forms
    }
    return render(request, 'university/edit_registration.html',context=context)
def read_registration(request, pk):
    return render(request, 'university/read_registration.html')