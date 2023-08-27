from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField

CATEGORIES = (
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
    item = models.CharField(max_length=100, unique=True)
    ingredients = models.TextField()
    price = MoneyField(max_digits=8, decimal_places=2, default_currency='GBP')
    category = models.CharField(max_length=80, choices=CATEGORIES)
    image = models.ImageField(upload_to='assets')
    chef = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )  # The chef can be deleted but the menu the chef created won't be deleted
    status = models.IntegerField(choices=STATUS, default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    url = models.SlugField()

    def __str__(self) -> str:
        return self.item
