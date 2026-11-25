#!/usr/bin/env bash

set -e

cd "$(dirname "$0")"

cd lit_Backend

python -m pip install -r requirements.txt

python manage.py collectstatic --noinput

python manage.py migrate --noinput