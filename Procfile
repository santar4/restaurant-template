release: python manage.py migrate --noinput
web: gunicorn restaurant_demo.wsgi --log-file -
release: python manage.py migrate && python manage.py createsuperuser --no-input || echo "Superuser already exists or creation failed"
