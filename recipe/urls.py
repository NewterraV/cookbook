from django.urls import path

from recipe.apps import RecipeConfig
from recipe.views import add_product_to_recipe

app_name = RecipeConfig.name

urlpatterns = [
    path('r/', add_product_to_recipe, name='add_product_to_recipe')
]
