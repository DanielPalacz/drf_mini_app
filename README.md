# drf_mini_app
```
Mini project for DRF practise:
 - 1st Django app is related to DRF API (one endpoint)
 - 2nd Django app shows fetching DRF-API and displaying it  (one endpoint)
```

#

#### Preparation phase:
```
 - Install Django and DRF
 - Setup Django project
   djangoadmin startproject myste .

 - Run default migrations (to create tables related to default Django app registered in settings.py)
   python manage.py migrate
 
 - Create superuser
   python manage.py create superuser
   
 - Create 1st Django app: drf_api
   python manage.py startapp drf_api
 - Register new apps (in settings):
    "drf_api",
    "rest_framework"

 - Create Posts model and setup migrations:
   python manage.py makemigrations
   python manage.py migrate

 - Register new model in Admin area
   admin.site.register(Posts)
```