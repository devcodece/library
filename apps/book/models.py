from django.db import models
from apps.author.models import Author

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=50)
    release_date = models.DateField('Release Date')
    cover = models.ImageField(upload_to='cover')
    visits = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title