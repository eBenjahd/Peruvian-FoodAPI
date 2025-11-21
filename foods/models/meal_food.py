from django.db import models
from .meal import Meal
from .food import Food

class MealFood(models.Model):

    meal = models.ForeignKey(Meal, on_delete=models.CASCADE,related_name='meal_foods')
    food = models.ForeignKey(Food, on_delete=models.CASCADE,related_name='foods')
    quantity = models.FloatField(help_text="Amount in grams or units")

    class Meta: 
        # Prevents duplicate in the same meal
        unique_together = ('meal','food')
        
    def __str__(self):
        return f"{self.food.name} in {self.meal.name} - {self.quantity}"