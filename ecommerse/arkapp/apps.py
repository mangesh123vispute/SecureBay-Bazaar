import arkapp
from django.apps import AppConfig


class ArkappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'arkapp'
    
    def ready(self):
        import arkapp.signals
