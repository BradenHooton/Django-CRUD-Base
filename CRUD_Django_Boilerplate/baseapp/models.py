from typing import Any
from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.ManyToManyField('Ingredient')
    instructions = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='img/', blank=True, null=True)
    serving_size = models.IntegerField(blank=True, null=True)
    serving_size_unit = models.CharField(max_length=100, blank=True, null=True)

    cook_time = models.IntegerField(blank=True, null=True)
    protein = models.IntegerField(blank=True, null=True)
    carbs = models.IntegerField(blank=True, null=True)
    fats = models.IntegerField(blank=True, null=True)
    calories = models.IntegerField(blank=True, null=True)

    # tag = models.ForeignObject(to='Tag')

    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class Tag(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

class User(models.Model):
    username = models.CharField(max_length=100)
    user_id = models.IntegerField()

    def __str__(self):
        return self.username

class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return self.rating
    
    def calculate_rating(self):
        ratings = (Rating.objects.filter(recipe=self.recipe))/len(User.objects.all(filter(rating=self.rating)))
        return ratings


    














