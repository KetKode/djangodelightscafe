import datetime

from django.db import models
from django.urls import reverse

# Create your models here.
# Ingredients, MenuItem,
# RecipeRequirement, Purchase


class MenuItem(models.Model):
    """ Represents a single entry on the restaurant's menu """
    DRINK = "DR"
    BAKERY = "BA"
    MENU_ITEM_CHOICES = [
        (DRINK, "Drink"),
        (BAKERY, "Bakery")
        ]
    name = models.CharField(max_length=100, unique=True)
    price_per_entry = models.FloatField(default=0)
    item_image = models.ImageField(null=True, blank=True, upload_to="images/")
    menu_item_type = models.CharField(max_length=2, choices=MENU_ITEM_CHOICES, default="DRINK")
    description = models.TextField(max_length=150, null=False, default="Description")

    def __str__(self):
        return f"{self.name} / ${self.price_per_entry}"

    def available(self):
        return all(X.is_enough() for X in self.reciperequirement_set.all())

    def get_absolute_url(self):
        return "/menu"


class Ingredient(models.Model):
    """ Represents a single ingredient in the restaurant's inventory """
    name = models.CharField(max_length=100, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=10)
    price_per_unit = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/ingredients"


class RecipeRequirement(models.Model):
    """ Represents a single ingredient required to make a meal on the restaurant's menu """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    def is_enough(self):
        return self.quantity <= self.ingredient.quantity

    def __str__(self):
        return f"{self.menu_item}: {self.ingredient}"

    def get_absolute_url(self):
        return "/menu"


class Purchase(models.Model):
    """ Represents a single purchase of a meal on the restaurant's menu """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.menu_item} / {self.timestamp}"

    def get_absolute_url(self):
        return "/purchases"
