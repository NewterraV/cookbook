from django.db import models


NULLABLE = {"blank": True, "null": True}


class Ingredient(models.Model):
    """Ingredient модель."""

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Название продукта'
    )
    count_use = models.PositiveIntegerField(
        default=0,
        verbose_name='Счетчик использований'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ['name']


class Recipe(models.Model):
    """Recipe модель"""

    name = models.CharField(max_length=100, verbose_name='Название рецепта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['name']


class RecipeIngredient(models.Model):
    """Модель веса ингредиентов"""

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент',
    )
    weight = models.PositiveIntegerField(verbose_name='Вес в гр.')

    def __str__(self):
        return f'{self.ingredient} - {self.weight}'

    class Meta:
        verbose_name = 'Ингридиент для рецепта'
        verbose_name_plural = 'Ингридиенты для рецепта'
