from django.db import models
from apps.book.models import Book

# Create your models here.

class Reader(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=30)
    age = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Loan(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return self.book.title