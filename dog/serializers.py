from rest_framework import serializers
from .models import Dog

# associates model and expression
class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ('id', 'name', 'breed', 'age', 'favorite_human')