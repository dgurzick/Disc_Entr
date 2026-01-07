#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Change to project directory
cd disc_entr_project

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

# Initialize 24 steps data
python manage.py init_24steps
