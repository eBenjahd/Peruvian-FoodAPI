from django.db import models
from .category import Category

class Food(models.Model):

    name = models.CharField(max_length=100, unique=True)
    calories = models.FloatField(default=0) #kcal
    protein = models.FloatField(default=0) #grams
    carbs = models.FloatField(default=0)
    fats = models.FloatField(default=0)
    fiber = models.FloatField(default=0)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='foods'
    )

    def __str__(self):
        return self.name