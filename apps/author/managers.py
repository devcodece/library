from django.db import models
#Importar la funcion Q
from django.db.models import Q

class AuthorManager(models.Manager):
    """ managers para el modelo Author """
    def search_author(self, kword):

        result = self.filter(
            name__icontains = kword
        )

        return result
    
    def search_author_two(self, kword):

        result = self.filter(
            Q(name__icontains = kword) | Q(last_name__icontains = kword)
        )

        return result