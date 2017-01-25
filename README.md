# Django 1.10+ project template

[![Dependency Status](https://gemnasium.com/jpadilla/django-project-template.svg)](https://gemnasium.com/jpadilla/django-project-template)

## Features

- Django 1.10 with GeoDjango.
- Development, Staging and Production settings with [django-configurations](https://django-configurations.readthedocs.org).
- Get value insight and debug information while on Development with [django-debug-toolbar](https://django-debug-toolbar.readthedocs.org).
- Load environment variables from `.env` with [django-dotenv](https://github.com/jpadilla/django-dotenv).
- Collection of custom extensions with [django-extensions](http://django-extensions.readthedocs.org).
- HTTPS and other security related settings on Staging and Production.
- PostgreSQL database support with psycopg2.
- PostGIS support.

## How to install

```bash
$ django-admin.py startproject \
  --template=https://github.com/jpadilla/django-project-template/archive/master.zip \
  --name=Procfile \
  --extension=py,md,env \
  project_name
$ mv example.env .env
$ pip install -r requirements.txt -r requirements/dev.txt
```

## Environment variables

These are common between environments. The `ENVIRONMENT` variable loads the correct settings, possible values are: `DEVELOPMENT`, `STAGING`, `PRODUCTION`.

```
ENVIRONMENT='DEVELOPMENT'
DJANGO_SECRET_KEY='dont-tell-eve'
DJANGO_DEBUG='yes'
```

These settings(and their default values) are only used on staging and production environments.

```
DJANGO_SESSION_COOKIE_SECURE='yes'
DJANGO_SECURE_BROWSER_XSS_FILTER='yes'
DJANGO_SECURE_CONTENT_TYPE_NOSNIFF='yes'
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS='yes'
DJANGO_SECURE_HSTS_SECONDS=31536000
DJANGO_SECURE_REDIRECT_EXEMPT=''
DJANGO_SECURE_SSL_HOST=''
DJANGO_SECURE_SSL_REDIRECT='yes'
DJANGO_SECURE_PROXY_SSL_HEADER='HTTP_X_FORWARDED_PROTO,https'
```

## Deployment

It is possible to deploy to Heroku or Self Hosted.

### Heroku

```bash
$ heroku create
$ heroku buildpacks:set https://github.com/cyberdelia/heroku-geo-buildpack.git
$ heroku buildpacks:add heroku-buildpack-python
$ heroku addons:add heroku-postgresql:dev
$ heroku pg:promote DATABASE_URL
$ heroku config:set ENVIRONMENT=PRODUCTION
$ heroku config:set DJANGO_SECRET_KEY=`./manage.py generate_secret_key`
```

You will also need to login to the postgresql database manually and run:

### Self Hosted

```bash
$ echo "Add instructions here."
```

```
CREATE EXTENSION postgis;
```

The easiest thing to do at this point is probably to run heroku push again.
