# Prep
## Create a virtual env
1. ```python -m venv env```
2. Select an interpreter
3. Install django: ```pip3 install django```

## Create a project
1. ```django-admin startproject [name] .``` Make sure to use the dot! (creates it in current directory)
2. Check if it works: ```python manage.py runserver```

## Take care of migrations
1. ```python manage.py migrate```
2. While further in project, make sure to always do a dry run ```python manage.py makemigrations --dry-run```
3. ```python manage.py migrate --plan```

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
7. Add a section EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
8. Add account creation settings and set redirect to /success.
    - Log in and go to /accounts/login. Use superuser creds. You'll get the confirm-email page.
    - Superuser was created before this setting, so confirm manually: go to email addresses, add new one, check verified and primary. Save all and exit.
    - Go back to /accounts/login and log in. You should see the URL /success.
    - If so, change the redirect back to /.
- Use ```pip3 freeze > requirements.txt``` to save all requirements.
- Create a directory called templates in the root folder and create a directory in it called allauth.
- Now commit changes.



