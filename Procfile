release: venv/Scripts/activate
release: python manage.py makemigrations
release: python manage.py migrate

web: gunicorn interop.wsgi