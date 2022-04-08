release: python manage.py migrate
web: gunicorn python manage.py collectstatic --no-input; governance.wsgi