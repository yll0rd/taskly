from django.apps import AppConfig


class BackgroundJobsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'background_jobs'

    def ready(self):
        import background_jobs.tasks
