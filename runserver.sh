#!/usr/bin/env bash

cd src/
cd spam_reports_project/
export PYTHONPATH=spam_reports_project;$PYTHONPATH

python manage.py migrate
python manage.py initadmin
python manage.py runserver 0.0.0.0:8000