from . import views
from django.urls import path

app_name = 'form'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_user/', views.add_user, name='add_user'),
    path('edit_user/', views.edit_user, name='edit_user'),
    path('delete_user/', views.delete_user, name='delete_user')
]