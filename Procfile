release: python manage.py makemigrations
release: python manage.py migrate

web: gunicorn mac.wsgi
heroku config:set DEBUG_COLLECTSTATIC=1
heroku ps:scale web=1
