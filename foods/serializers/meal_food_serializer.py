from rest_framework import serializers
from foods.models import MealFood
from .food_serializer import FoodSerializer

class MealFoodSerializer(serializers.ModelSerializer):
    food = FoodSerializer(read_only=True)

    class Meta:
        model = MealFood
        fields = ['id', 'meal', 'food', 'quantity']