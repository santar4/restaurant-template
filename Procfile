release: pip install -r requirements.txt && python manage.py migrate && python manage.py populate_data
web: gunicorn restaurant_demo.wsgi