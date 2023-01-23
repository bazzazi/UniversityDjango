from django.urls import path
from . import views

urlpatterns=[
    # Index
    path('<str:id>',views.index,name='index'),
    # Student
    path('student/add/',views.add_student,name='add_student'),
    path('student/remove/<str:pk>',views.remove_student,name='remove_student'),
    path('student/edit/<str:pk>',views.edit_student,name='edit_student'),
    path('student/read/<str:pk>',views.read_student,name='read_student'),
    # Course
    path('course/add/',views.add_course,name='add_course'),
    path('course/remove/<str:pk>',views.remove_course,name='remove_course'),
    path('course/edit/<str:pk>',views.edit_course,name='edit_course'),
    path('course/read/<str:pk>',views.read_course,name='read_course'),
    # Content
    path('content/add/',views.add_content,name='add_content'),
    path('content/remove/<str:pk>',views.remove_content,name='remove_content'),
    path('content/edit/<str:pk>',views.edit_content,name='edit_content'),
    path('content/read/<str:pk>',views.read_content,name='read_content'),
    # Regitration
    path('registration/add/',views.add_registration,name='add_register'),
    path('registration/remove/<str:pk>',views.remove_registration,name='remove_register'),
    path('registration/edit/<str:pk>',views.edit_registration,name='edit_register'),
    path('registration/read/<str:pk>',views.read_registration,name='read_register'),
]