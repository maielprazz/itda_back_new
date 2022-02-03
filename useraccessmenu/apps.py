from django.apps import AppConfig


class UseraccessmenuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'useraccessmenu'

    def ready(self):
        import useraccessmenu.signals

