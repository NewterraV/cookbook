from django.urls import path

from recipe.apps import RecipeConfig
from recipe.views import add_product_to_recipe, cook_recipe

app_name = RecipeConfig.name

urlpatterns = [
    path('product/add/', add_product_to_recipe, name='add_product_to_recipe'),
    path('cook/', cook_recipe, name='cook_recipe')
]
