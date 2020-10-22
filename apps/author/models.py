from django.db import models
from . managers import AuthorManager

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=30)
    age = models.PositiveIntegerField()

    objects = AuthorManager()

    def __str__(self):
        return self.name + '-' + self.last_name