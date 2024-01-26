from django.shortcuts import render
from recipe import service
from django.http import HttpResponse


def add_product_to_recipe(request):
    if request.method == 'GET':
        status = service.add_product_to_recipe(request.GET)

        return HttpResponse(status=status)


def cook_recipe(request):
    if request.method == 'GET':
        status = service.cook_recipe(request.GET['recipe_id'])

        return HttpResponse(status=status)
