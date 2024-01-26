from django.test import TestCase

from recipe.models import Recipe, Ingredient, RecipeIngredient
from recipe.service import add_product_to_recipe, cook_recipe


class TestMixin:

    @staticmethod
    def get_create_content():
        """Метод создает контент пользователем через запрос"""
        ing_data = [
            Ingredient(name='test', count_use=0),
            Ingredient(name='test1', count_use=0),
            Ingredient(name='test2', count_use=0),
        ]
        Ingredient.objects.bulk_create(ing_data)
        ing_1 = Ingredient.objects.get(name='test1')
        ing_2 = Ingredient.objects.get(name='test2')
        recipe = Recipe.objects.create(name='test')
        recipe_ing = [
            RecipeIngredient(recipe=recipe, ingredient=ing_1, weight=100),
            RecipeIngredient(recipe=recipe, ingredient=ing_2, weight=100),
        ]
        RecipeIngredient.objects.bulk_create(recipe_ing)


class TestAddProductToRecipe(TestMixin, TestCase):

    def setUp(self):
        self.get_create_content()

    def test_add_product_to_recipe(self):
        recipe_id = Recipe.objects.get(name='test').pk
        product_id = Ingredient.objects.get(name='test1').pk
        weight = 300
        data = {'recipe_id': recipe_id, 'product_id': product_id,
                'weight': weight}

        response = add_product_to_recipe(data)
        ing = RecipeIngredient.objects.get(ingredient=product_id)

        self.assertEqual(response, 202)
        self.assertEqual(ing.weight, weight)
        self.assertEqual(RecipeIngredient.objects.count(), 2)

        data['weight'] = 200
        data['product_id'] = Ingredient.objects.get(name='test').pk

        response = add_product_to_recipe(data)
        self.assertEqual(response, 201)
        self.assertEqual(RecipeIngredient.objects.count(), 3)

    def test_cook_recipe(self):
        recipe_id = Recipe.objects.get(name='test').pk

        result = cook_recipe(recipe_id)
        recipe_ing = RecipeIngredient.objects.select_related(
            'ingredient').filter(recipe=recipe_id)
        ing = [item.ingredient for item in recipe_ing]

        self.assertEqual(result, 202)
        self.assertEqual(ing[0].count_use, 1)
        self.assertEqual(ing[1].count_use, 1)
