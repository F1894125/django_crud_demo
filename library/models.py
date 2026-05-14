from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.SlugField(max_length=20)
    summary = models.TextField(max_length=500)

    def __str__(self):
        return self.title