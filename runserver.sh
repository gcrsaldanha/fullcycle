#!/bin/bash
python manage.py migrate --settings=$DJANGO_SETTINGS_MODULE
python manage.py create_superuser --settings=$DJANGO_SETTINGS_MODULE
python manage.py seed_database --settings=$DJANGO_SETTINGS_MODULE
python manage.py runserver 0.0.0.0:8000 --settings=$DJANGO_SETTINGS_MODULE
