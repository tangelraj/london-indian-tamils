#!/usr/bin/env bash

set -o errexit

cd lit_backend

python -m pip install -r requirements.txt

python manage.py collectstatic --noinput

python manage.py migrate --noinput