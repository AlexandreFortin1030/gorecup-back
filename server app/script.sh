#!/bin/bash

echo "apply database migrations"
python manage.py migrate
python manage.py makemigrations

echo "Starting django sever"

python manage.py runserver
exec "$@"
