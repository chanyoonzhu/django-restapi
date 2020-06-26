from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Dog
from .serializers import DogSerializer

# Create your views here.

class DogList(ListAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

