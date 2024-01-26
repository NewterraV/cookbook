from typing import List, Dict

from django.db.models import Q, F

from recipe.models import Recipe, RecipeIngredient, Ingredient


def add_product_to_recipe(params: Dict[str, str]) -> int:
    """
    Функция добавляет к указанному рецепту указанный продукт с указанным
    весом. Если в рецепте уже есть такой продукт, то функция меняет его
    вес в этом рецепте на указанный.
    :param params:
    :return:
    """
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


def cook_recipe(recipe_id: int) -> int:
    """
    Функция увеличивает на единицу количество приготовленных блюд для
    каждого продукта, входящего в указанный рецепт.
    :param recipe_id: ID рецепта
    :return:
    """
    recipe_ing = RecipeIngredient.objects.select_related(
        'ingredient').filter(recipe_id=recipe_id)
    ing = [item.ingredient for item in recipe_ing]

    for item in ing:
        item.count_use = F('count_use') + 1

    Ingredient.objects.bulk_update(ing, ["count_use"], batch_size=100)

    return 202


def get_recipes_without_product(product_id: int) -> List[Recipe]:
    """
    Метод получает ID продукта(ингредиента) и возвращает список рецептов, где
    данный продукт не используется либо присутствует в количестве меньше 10
    грамм.
    :param product_id: ID продукта/ингредиента
    :return:
    """
    query = RecipeIngredient.objects.filter(
        ingredient__id=product_id, weight__gte=10
    ).values_list('recipe_id', flat=True)
    queryset = Recipe.objects.exclude(
        id__in=query)
    return queryset
