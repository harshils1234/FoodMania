from django.apps import AppConfig


class FoodmaniaWebsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'foodmania_website'

    def ready(self):
        from . import signals
