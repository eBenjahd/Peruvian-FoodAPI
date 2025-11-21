from rest_framework import serializers
from foods.models import Food
from .category_serializer import CategorySerializer

class FoodSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)

    class Meta:
        model = Food
        fields = [
            'id',
            'name',
            'calories',
            'protein',
            'carbs',
            'fats',
            'fiber',
            'category',
        ]