from django.db import models


class User(models.Model):
    username = models.CharField(max_length=15, unique=True, verbose_name='Имя')
    password = models.CharField(max_length=15, verbose_name='Пароль')
    user_date_add = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Categories(models.Model):
    category_name = models.CharField(max_length=30, verbose_name='Категория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Recipes(models.Model):
    recipe_name = models.CharField(max_length=100, verbose_name='Название')
    recipe_description = models.TextField(verbose_name='Описание')
    ingredients = models.TextField(verbose_name='Ингредиенты')
    stages_preparation = models.TextField(verbose_name='Этапы приготовления')
    time_preparation = models.IntegerField(verbose_name='Время приготовления, мин.')
    food_image = models.ImageField(upload_to='food_images', blank=True, verbose_name='Изображение')
    author = models.CharField(max_length=20, verbose_name='Автор')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class RecipeCategoryFilter(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, verbose_name='Рецепт')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name = 'Рецепты по категориям'
        verbose_name_plural = 'Рецепты по категориям'
