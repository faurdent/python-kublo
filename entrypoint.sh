#!/bin/sh
set -e

until cd /app
do
    echo "Wait for server volume..."
done

until python manage.py migrate
do
    echo "Waiting for postgres ready..."
done

python manage.py collectstatic --no-input

gunicorn core.wsgi:application --bind 0.0.0.0 --workers 4 --threads 4