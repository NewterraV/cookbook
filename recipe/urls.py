from django.urls import path

from recipe.apps import RecipeConfig
from recipe.views import (add_product_to_recipe, cook_recipe,
                          IngredientListView)

app_name = RecipeConfig.name

urlpatterns = [
    path('product/add/',
         add_product_to_recipe,
         name='add_product_to_recipe'
         ),
    path('cook/',
         cook_recipe,
         name='cook_recipe'
         ),
    path('<int:pk>/show/',
         IngredientListView.as_view(),
         name='show_recipes_without_product'
         ),
]
