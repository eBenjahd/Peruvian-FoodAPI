from rest_framework import serializers
from foods.models import Meal
from .meal_food_serializer import MealFoodSerializer

class MealSerializer(serializers.ModelSerializer):

    foods = MealFoodSerializer(source = 'mealfood', many = True, read_only = True)
    class Meta:

        model = Meal
        fields = ['id', 'user', 'date', 'foods']