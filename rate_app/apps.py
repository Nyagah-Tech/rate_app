from django.apps import AppConfig


class RateAppConfig(AppConfig):
    name = 'rate_app'
    
    def ready(self):
        import rate_app.signals
