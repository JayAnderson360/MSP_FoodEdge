@ECHO OFF

cmd /k ".\Django-env\Scripts\activate & py manage.py makemigrations & py manage.py migrate & py manage.py runserver"

