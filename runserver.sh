#!/usr/bin/env bash
ENV DJANGO_DB_NAME=spamreports
ENV DJANGO_SU_NAME=admin
ENV DJANGO_SU_EMAIL=admin@admin.com
ENV DJANGO_SU_PASSWORD=admin1234

cd src/spam_reports_project
export PYTHONPATH=src/spam_reports_project;$PYTHONPATH

python manage.py migrate
python -c "import os
    os.environ['DJANGO_SETTINGS_MODULE'] = 'project_name.settings'
    import django
    django.setup()
    from django.contrib.auth.management.commands.createsuperuser import get_user_model
    if get_user_model().objects.filter(username='$DJANGO_SUPERUSER_USERNAME'):
        print 'Super user already exists. SKIPPING...'
    else:
        print 'Creating super user...'
        get_user_model()._default_manager.db_manager('$DJANGO_DB_NAME').create_superuser(username='$DJANGO_SUPERUSER_USERNAME', email='$DJANGO_SUPERUSER_EMAIL', password='$DJANGO_SUPERUSER_PASSWORD')
        print 'Super user created...'"
python manage.py runserver 0.0.0.0:8000