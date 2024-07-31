from django.urls import path
from .views import *

urlpatterns = [
    path('', recipe_list, name='recipe_list'),
    path('create/', recipe_create, name='recipe_create'),
    path('update/<int:pk>/', recipe_update, name='recipe_update'),
    path('delete/<int:pk>/', recipe_delete, name='recipe_delete'),
]

