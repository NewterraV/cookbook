from django.views.generic import ListView
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from recipe import service
from recipe.models import Ingredient, Recipe


def add_product_to_recipe(request):
    """
    Функция добавляет к указанному рецепту указанный продукт с указанным
    весом. Если в рецепте уже есть такой продукт, то функция меняет его
    вес в этом рецепте на указанный.
    Пример запроса:
        http://127.0.0.1:8000/recipe/product/add/?recipe_id=1&product_id=4&weight=230
    @params запроса:
        @recipe_id: ID рецепта
        @product_id: ID продукта(ингредиента)
        @weight: Вес ингредиента
    """
    if request.method == 'GET':
        get_object_or_404(Recipe, pk=request.GET.get('recipe_id'))
        get_object_or_404(Ingredient, pk=request.GET.get('product_id'))

        with transaction.atomic():
            status = service.add_product_to_recipe(request.GET)
        return HttpResponse(status=status)

    return HttpResponse(status=405)


def cook_recipe(request):
    """
    Функция увеличивает на единицу количество приготовленных блюд для
    каждого продукта, входящего в указанный рецепт.
    @params запроса:
        @recipe_id: ID рецепта
    """
    if request.method == 'GET':
        get_object_or_404(Recipe, pk=request.GET.get('recipe_id'))

        with transaction.atomic():
            status = service.cook_recipe(request.GET['recipe_id'])
        return HttpResponse(status=status)

    return HttpResponse(status=405)


class IngredientListView(ListView):
    """
    Метод получает ID продукта(ингредиента) и возвращает список рецептов, где
    данный продукт не используется либо присутствует в количестве меньше 10
    грамм.
    Пример запроса:
        http://127.0.0.1:8000/recipe/cook/?recipe_id=18
    @params запроса:
         @product_id : ID продукта(ингредиента)
    """
    model = Ingredient
    template_name = 'recipe/recipe.html'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        get_object_or_404(Ingredient, pk=pk)
        queryset = service.get_recipes_without_product(pk)
        return queryset
