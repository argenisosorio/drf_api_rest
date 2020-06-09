# Django Rest Framework - Example
Read json generated by django rest framework in a template

## Requirements
```
Python==2.7.3
Django==1.9.5
djangorestframework==3.5.0
requests==2.23.0
```

## Run Project
```
$ pip install -r requirements.txt
$ python manage.py makemigrations app
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

See results in:

[http://127.0.0.1:8000/users/?format=json](http://127.0.0.1:8000/users/?format=json)

See json with users

[http://127.0.0.1:8000/index](http://127.0.0.1:8000/index)

See the table with the list of users
