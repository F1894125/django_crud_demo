from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_student/', views.add_student, name='add_student'),
    path('edit_student/', views.edit_student, name='edit_student'),
    path('view_student/', views.view_student, name='view_student'),
    path('delete_student/', views.delete_student, name='delete_student'),
]