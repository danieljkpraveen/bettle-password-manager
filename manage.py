from settings.apps_config import APPS
from settings.database_config import DATABASE_CONFIG


def base_django():
    import django
    from django.conf import settings
    
    if settings.configured:
        return
    
    settings.configure(
        INSTALLED_APPS = APPS,
        DATABASES = DATABASE_CONFIG,
    )
    django.setup()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    base_django()
    execute_from_command_line()
    