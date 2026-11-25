#!/usr/bin/env bash

set -e

cd lit_Backend

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Creating media directory..."
mkdir -p media

echo "Restoring existing website images..."

if [ -d ../lit_frontend/static/website_media ]; then
    cp -rn ../lit_frontend/static/website_media/. media/
fi

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Build completed successfully!"