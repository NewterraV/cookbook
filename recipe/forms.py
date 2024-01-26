from django import forms
from django.core.exceptions import ValidationError

from recipe.models import RecipeIngredient


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['recipe', 'ingredient', 'weight']
        read_only_fields = ['recipe']


class RecipeIngredientFormset(forms.models.BaseInlineFormSet):

    def clean(self):
        super(RecipeIngredientFormset, self).clean()
        ingredients = []
        for form in self.forms:
            if not hasattr(form, 'cleaned_data'):
                continue
            ing = form.cleaned_data.get('ingredient')
            if ing:
                ingredients.append(form.cleaned_data.get('ingredient').pk)
        if len(ingredients) != len(set(ingredients)):
            raise ValidationError('Один и тот же ингредиент не может '
                                  'быть использован дважды в одном рецепте')
