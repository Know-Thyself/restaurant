from django.db import models
from django.contrib.auth.models import User

MEAL_CATEGORY = (
    ('starters', 'Starters'),
    ('salads', 'Salads'),
    ('main_dishes', 'Main Dishes'),
    ('desserts', 'Desserts'),
)

STATUS = (
    (0, 'Unavailable'),
    (1, 'Available'),
)


class Menu(models.Model):
    meal = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    meal_type = models.CharField(max_length=80, choices=MEAL_CATEGORY)
    chef = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )  # The chef can be deleted but the menu the chef created won't be deleted
    status = models.IntegerField(choices=STATUS, default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.meal
