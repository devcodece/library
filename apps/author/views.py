from django.shortcuts import render
from django.views.generic import ListView
from . models import Author
# Create your views here.

class ListAuthors(ListView):
    #model = Author
    context_object_name = 'list_authors'
    template_name = 'author/list.html'

    def get_queryset(self):
        key_word = self.request.GET.get('kword')
        return Author.objects.search_author_two(key_word)