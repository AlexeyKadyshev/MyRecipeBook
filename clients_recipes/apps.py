from django.apps import AppConfig


class ClientsRecipesConfig(AppConfig):
    verbose_name = 'Рецепты наших пользователей'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clients_recipes'
