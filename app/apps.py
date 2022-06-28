from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'app'
    def ready(self):
        print("========== signals being imported =========")
        import app.mysignals
