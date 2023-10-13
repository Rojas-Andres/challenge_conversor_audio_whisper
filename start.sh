#!/bin/sh

python3.9 manage.py migrate --noinput
python3.9 manage.py runserver 0.0.0.0:80

exec "$@"