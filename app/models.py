from django.db import models
from django.core.exceptions import ValidationError

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title