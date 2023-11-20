from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from App.models import *
from .serializers import *

class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

