from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', include('form.urls', namespace='form')),
    path('fuzzy/', include('fuzzy.urls', namespace='fuzzy')),
    path('student/', include('student.urls', namespace='student')),
]
