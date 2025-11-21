from django.db import models
from django.contrib.auth.models import User

class Meal(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='meals')
    name = models.CharField(max_length = 50)
    date = models.DateField(auto_now_add = True)

    def __str__(self):
        return f'{self.name} - {self.user.username}'