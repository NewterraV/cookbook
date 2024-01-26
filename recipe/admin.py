from django.contrib import admin
from recipe.models import Recipe, Ingredient, RecipeIngredient
from recipe.forms import RecipeIngredientFormset


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    formset = RecipeIngredientFormset
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Админка рецептов"""

    list_display = 'name',
    fields = 'name',
    inlines = RecipeIngredientInline,


@admin.register(Ingredient)
class IngredientModelAdmin(admin.ModelAdmin):
    """Админка Ингридиентов"""
    list_display = 'name', 'count_use'
    fields = 'name',
    readonly_fields = 'count_use',
