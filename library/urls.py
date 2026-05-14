from django.urls import path, include
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_book/', views.add_book, name='add_book'),
    path('show_books/', views.show_books, name='show_books'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book')
]