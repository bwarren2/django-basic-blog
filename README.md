




# Django-Basic-Blog ![Build Status](https://circleci.com/gh/bwarren2/django-basic-blog.png?circle-token=695d40953b8186ef34f929442d314cf893d4f187&style=shield)

DBB is a dead simple blog app.  It has entries and an RSS feed; not much else.  Entries are expected to be in raw html.

## Quick start

Install with pip

    pip install django-basic-blog

Add "blog" to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = (
        ...
        'blog',
    )

Include the blog URLconf in your project urls.py like this:

    url(r'^blog/', include('blog.urls', namespace='blog')),

Run `python manage.py migrate` to create the blog models.

Add the settings vars for RSS fields:

    BLOG_TITLE  // Default "My Blog"
    BLOG_DESCRIPTION  // Default "I have a Django Blog!"

and the override the default entries/page and RSS pagination if you want

    BLOG_ENTRIES_PER_PAGE  // Default 20
    BLOG_ENTRIES_PER_RSS  // Default 5

Start the development server and visit http://127.0.0.1:8000/admin/
   to create an entry (you'll need the Admin app enabled).

Visit http://127.0.0.1:8000/blog/ to see the blog.

*NOTE*:  There is support for each entry having associated js, but you need work that into the templates yourself.  Be careful.

## Development and Testing


### Development

Make a venv, install django.

Set env var to the test settings

export PYTHONPATH='/home/ben/Projects/django-basic-blog'
export DJANGO_SETTINGS_MODULE='sample_project.settings'

Start the server with `django-admin runserver`.

(If you want the admin to be pretty, try collecting statics.)

To poke around with creating and displaying entries:

Set up a superuser (`django-admin createsuperuser`) and hit the admin at `/admin` to try stuff out.

### Testing

`django-admin test blog --settings=sample_project.settings`
