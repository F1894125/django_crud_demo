from django.urls import path
from . import views

app_name = "sessions_sandbox"

urlpatterns = [
    path('', views.home, name='home'),
    path('find_elements/', views.find_elements, name='find_elements'),
    path('add_elements/', views.add_elements, name='add_elements'),
    path('reset_session/', views.reset_session, name='reset_session'),
]