from django.db.models import Prefetch, Q, F

from recipe.models import Recipe, RecipeIngredient, Ingredient

from django.db import connection, reset_queries
import time
import functools


def query_debugger(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        reset_queries()

        start_queries = len(connection.queries)

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        end_queries = len(connection.queries)

        print(f"Function : {func.__name__}")
        print(f"Number of Queries : {end_queries - start_queries}")
        print(f"Finished in : {(end - start):.2f}s")
        return result

    return inner_func


@query_debugger
def add_product_to_recipe(params):
    """Метод добавляет/обновляет ингредиент рецепта"""
    recipe_id = params['recipe_id']
    product_id = params['product_id']
    weight = params['weight']
    ing = RecipeIngredient.objects.select_related(
        'recipe', 'ingredient').filter(
        Q(recipe_id=recipe_id) & Q(ingredient=product_id)).first()

    if ing:
        ing.weight = weight
        ing.save()
        return 202

    recipe = Recipe.objects.get(id=recipe_id)
    ingredient = Ingredient.objects.get(id=product_id)
    RecipeIngredient.objects.create(
        recipe=recipe,
        ingredient=ingredient,
        weight=weight
    )
    return 201


@query_debugger
def cook_recipe(recipe_id: int) -> int:

    recipe_ing = RecipeIngredient.objects.select_related(
        'ingredient').filter(recipe_id=recipe_id)
    ing = [item.ingredient for item in recipe_ing]

    for item in ing:
        item.count_use = F('count_use') + 1

    Ingredient.objects.bulk_update(ing, ["count_use"], batch_size=100)

    return 202
