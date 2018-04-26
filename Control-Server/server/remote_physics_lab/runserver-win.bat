@ECHO Off
REM Runs the server at http://127.0.0.1:8000
ECHO Running the server...
python manage.py makemigrations
python manage.py migrate
python manage.py runserver