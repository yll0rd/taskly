#!/bin/bash

echo "Activating Environment..."
python3 -m venv venv
source venv/bin/activate

echo "Building the project..."
# Build the project
python3 -m pip install --use-pep517 -r requirements.txt

echo "Make Migration..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collect Static..."
python3 manage.py collectstatic --noinput --clear
