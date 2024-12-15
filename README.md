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



#

#### DRF API:
```
   A. SERIALIZER
   B. CLASS-BASED VIEW
   C. URL LINKING (ROUTER)

A)
 - Telling to DRF about the model and how should serialize the data.
   CREATE SERIALIZER: DB <-> SERIALIZER <-> VIEW 
   serializer.py
   DRF has set of serializers
   here, there is used 'serializers.HyperlinkedModelSerializer'

B)
 - Creating class-based view
   here, there is used DRF provided class-based view: 'viewsets.ModelViewSet':

C) 
 - Url linking
   mysite.urls
   drf_api.urls
       creating default router
           it auto-generates documentation and endpoints to ViewSets
```


#

#### Django single-endpoint app showing DRF-API data