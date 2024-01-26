from django.views.generic import ListView

from recipe import service
from django.http import HttpResponse

from recipe.models import Ingredient


def add_product_to_recipe(request):
    """
    Функция добавляет к указанному рецепту указанный продукт с указанным
    весом. Если в рецепте уже есть такой продукт, то функция меняет его
    вес в этом рецепте на указанный.
    @params запроса:
        @recipe_id: ID рецепта
        @product_id: ID продукта(ингредиента)
        @weight: Вес ингредиента
    """
    if request.method == 'GET':
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
        status = service.cook_recipe(request.GET['recipe_id'])
        return HttpResponse(status=status)
    return HttpResponse(status=405)


class IngredientListView(ListView):
    """
    Метод получает ID продукта(ингредиента) и возвращает список рецептов, где
    данный продукт не используется либо присутствует в количестве меньше 10
    грамм.
    @params запроса:
         @product_id : ID продукта(ингредиента)
    """
    model = Ingredient
    template_name = 'recipe/recipe.html'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = service.get_recipes_without_product(pk)
        return queryset
