web: gunicorn mac.wsgi:application --log-file - --log-level debug
heroku ps:scale web=2
python manage.py collectstatic --noinput
manage.py migrate

