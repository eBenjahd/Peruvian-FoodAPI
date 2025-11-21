from django.contrib import admin
from .models import Food, Meal, MealFood, Category

admin.site.register(Food)
admin.site.register(Meal)
admin.site.register(MealFood)
admin.site.register(Category)
