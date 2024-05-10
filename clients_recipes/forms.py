from django import forms

from .models import User, Recipes, Categories, RecipeCategoryFilter


class LoginForm(forms.Form):
    username = forms.CharField(min_length=5, max_length=25, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, min_length=5, max_length=25, label='Пароль')
    confirm_password = forms.CharField(widget=forms.PasswordInput, min_length=5, max_length=25,
                                       label='Подтвердите пароль')


class EntranceForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=25, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, min_length=5, max_length=25, label='Пароль')


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['recipe_name', 'recipe_description', 'ingredients', 'stages_preparation', 'time_preparation',
                  'food_image', 'author']
        widgets = {
            'recipe_description': forms.Textarea(attrs={'cols': 50, 'rows': 3}),
            'stages_preparation': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
            'ingredients': forms.Textarea(attrs={'cols': 50, 'rows': 5})
        }


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['category_name']


class RecipeCategoryFilterForm(forms.Form):
    recipes = Recipes.objects.all()
    recipes_choices = [(recipe.id, recipe.recipe_name) for recipe in recipes]
    recipe = forms.ChoiceField(choices=recipes_choices, required=False, label='Рецепт')
    categories = Categories.objects.all()
    category_choices = [(category.id, category.category_name) for category in categories]
    category = forms.ChoiceField(choices=category_choices, required=False, label='Категория')