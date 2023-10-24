#!/bin/sh

python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py makemigrations stamp --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput --clear

exec "$@"
fi