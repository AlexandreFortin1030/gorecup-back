#!/bin/bash

echo "apply database migrations"
python manage.py makemigrations
python manage.py migrate


echo "Starting django sever"

python manage.py runserver
exec "$@"
