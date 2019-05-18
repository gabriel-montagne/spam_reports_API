#!/usr/bin/env bash

cd src/
cd spam_reports_project/
export PYTHONPATH="$PYTHONPATH:/code/src/spam_reports_project/spam_reports_project"

python manage.py migrate
python manage.py initadmin
python manage.py runserver 0.0.0.0:8000