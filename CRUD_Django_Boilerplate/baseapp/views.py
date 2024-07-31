from pydoc import describe
from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipe_create(request):
    if request.method == 'POST':
        title  = request.POST['title']
        description = request.POST.get('description')
        Recipe.objects.create(title=title, description=description)
        return redirect('recipe_list')
    return render(request, 'recipes/recipe_create.html')

def recipe_update(request, pk):
    recipe = Recipe.objects.get(id=pk)
    if request.method == 'POST':
        recipe.title = request.POST['title']
        recipe.description = request.POST['description']
        recipe.save()
        return redirect('recipe_list')
    return render(request, 'recipes/recipe_update.html', {'recipe': recipe})

def recipe_delete(request, pk):
    recipe = Recipe.objects.get(id=pk)
    recipe.delete()
    return redirect('recipe_list')


















