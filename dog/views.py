from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Dog
from .serializers import DogSerializer

# Create your views here.

class DogList(ListAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class DogDetail(RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

