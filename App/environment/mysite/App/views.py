from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import *

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'


