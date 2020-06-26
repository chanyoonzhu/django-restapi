from django.urls import path
from .views import DogList

urlpatterns = [
    path('', DogList.as_view(), name='dog_list')
]