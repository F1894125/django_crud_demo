from django.urls import path
from . import views

app_name = 'fuzzy'

urlpatterns = [
    path('', views.home, name='home'),
    path('triangular/', views.fuzzy_triangular, name='fuzzy_triangular'),
    path('trapezoidal/', views.fuzzy_trapezoidal, name='fuzzy_trapezoidal'),
    path('gaussian/', views.fuzzy_gaussian, name='fuzzy_gaussian'),
    path('fuzzy_crisp/', views.fuzzy_crisp, name='fuzzy_crisp'),
    path('delete_test/', views.delete_test, name='delete_test'),
]