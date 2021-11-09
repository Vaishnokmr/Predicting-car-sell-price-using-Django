release: python manage.py makemigrations
release: python manage.py migrate

web: gunicorn mac.wsgi
heroku ps:scale web=1
