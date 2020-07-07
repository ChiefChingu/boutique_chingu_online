# Prep
## Create a virtual env
1. ```python -m venv env```
2. Select an interpreter
3. Install django: ```pip3 install django```

## Create a project
1. ```django-admin startproject [name] .``` Make sure to use the dot! (creates it in current directory)
2. Check if it works: ```python manage.py runserver```

## Secure secret key
- Create a file to isolate your secret key
- In this project it is called secret.py
- Cut and paste the secret key from settings.py in this file (remove from settings.py)
- Add ```from secret import SECRET_KEY``` to the settings file (to import the key)

## Create .gitignore
- Create the file in the root of the project
- Add:
    - *.sqlite3
    - *.pyc
    - ```__pycache__```
    - env
    - /env
    - secret.py

## Initiate repository and set remote
- ```git init```
- If not done yet: create repo in github.
- Do a first commit (add all there is and commit)
- Then:
    - ```git remote add origin https://github.com/ChiefChingu/reviewsfromkids.git```
    - ```git push -u origin master```

## Take care of migrations
1. ```python manage.py migrate```
2. While further in project, make sure to always do a dry run ```python manage.py makemigrations --dry-run```
3. ```python manage.py migrate --plan```

## Create superuser
- ```python manage.py createsuperuser```
- Choose username and password. Leave email blank.

# Project steps
## 1 Allauth
- ```pip3 install django-allauth```
- Adjust settings.py:
    1. In section TEMPLATES: make sure it contains ```django.template.context_processors.request'```. If it does, mark it as required just to be sure. This is necessary to access the HTTP request object in our templates. For instance, to use ```request.user``` or ```request.useremail``` in the django templates.
    2. Add AUTHENTICATION_BACKENDS as a new section. Needed to login by username or email. Not supported yet by django.
    3. Add some apps to the section INSTALLED_APPS
    4. Add ```SITE_ID = 1``` underneath AUTHENTICATION_BACKENDS
- Adjust url.py:
    5. Add Allauth URLs
    6. Import ```include```
- Run migrations to update the database since we added new apps: ```python manage.py migrate```
- Start the server and login into the /admin.
- You'll see that there is more info now after we added some apps.
- Go to the sites area and change the domain name and display name.
- Allauth sends confirmation mails to new accounts. To test this, we need to send these to the console, so we can use the confirmation links (alternatively, first create the whole signup flow and then test with temp emails)
7. Add a section ```EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'```
8. Add account creation settings and set redirect to /success.
    - Log in and go to /accounts/login. Use superuser creds. You'll get the confirm-email page.
    - Superuser was created before this setting, so confirm manually: go to email addresses, add new one, check verified and primary. Save all and exit.
    - Go back to /accounts/login and log in. You should see the URL /success.
    - If so, change the redirect back to /.
- Use ```pip3 freeze > requirements.txt``` to save all requirements.
- Create a directory called templates in the root folder and create a directory in it called allauth.
- Now commit changes.

## 2 Base template
- We need to copy the Allauth templates and use them in our templates folder. This way these customizable templates take precedence over the standard Allauth templates.
- To do so, go to the folder: env/lib/allauth/templates and copy all content.
- Paste the content in the templates/allauth folder in the root.
- Now it is time to create a base.html at project level.
- Create a new file in the templates folder called base.html
- Use bootstrap if preferred, otherwise materializecss.
- Grab the boilerplate template and copy in the base.html
- Customize the template:
    1. ```<meta http-equiv="X-UA-Compatible" content="ie=edge">``` to make it work with Internet Explorer
    - Change the title to match your project
    - Delete the Hello World heading
    - Move scripts to the header
    2. Add ```{% load static %}``` for when we need to load static files.
    3. Add some blocks to be able to customize later on:
        - Block for meta
        - Block for core CSS
        - Block for core JS
    4. Add a block in the title to be able to make the title page/template specific
    - Add header and messages block via if statement.
    - Add page header block.
    - Add main content block.
    - Add postload js block.

## 3. Add a homepage: create a home app
- ```python manage.py startapp home``` creates a home folder in the project root.
- ```mkdir -p home/templates/home``` to create a templates with a home folder in it.
- Create a file index.html in this home folder.
- Add template blocks and a test text.
1. Add a view to render the template in views.py
- Create a file urls.py in the home folder.
2. Copy the content from the project-level urls.py and paste it.
- Remove the comments and remove the ```include``` from the django import.
3. Add an empty path to indicate this is the route URL. ```path('', views.index, name='home'),``` It is going to render views.index with the name home.
4. We need to link the views.py in order to render it, so add it as import ```from . import views```.
5. We also need to add the urls that we specify in the home app to the project-level urls.py.
6. And add the home app to the installed apps in the settings.py.
7. Add the templates directories to the templates section in the DIRS:
    - ```os.path.join(BASE_DIR, 'templates'),```
    - ```os.path.join(BASE_DIR, 'templates', 'allauth'),```

## 4. Homepage content and styling
- Copy paste content from Code Institute into the index.html
- Copy paste content from Code Institute into the base.html
- Create new folders:
    - ```mkdir static```
    - ```mkdir media```
    - ```mkdir static/css```
- Create a css file base.css and copy code in it.
- Grab the image and upload in the media folder.
1. Grab the Google Font via fontsgoogle.com and add the code
2. Link the base.css file
3. Grab the fontawesomecode and paste
- Now we need to link the static and media files:
    4. In settings.py underneath STATIC_URL put ```STATICFILES_DIRS = os.path.join(BASE_DIR, 'static')``` so django knows where the static files are located
    5. Add MEDIA_URL and MEDIA_ROOT to set where uploaded media files go.
- To allow django to see the MEDIA_URL we go to urls.py:
    6. ```from django.conf import settings```
    7. ```from django.conf.urls.static import static```
    8. Add to urlpatterns ```+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)```

## 5. Add product data
- From kaggle.com you can get sample data.






## 3 Install SCSS