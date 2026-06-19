release: python manage.py migrate --noinput
web: gunicorn restaurant_demo.wsgi --log-file -
# release: python manage.py collectstatic --noinput