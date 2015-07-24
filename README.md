# Django-Basic-Blog

DBB is a dead simple blog app.  It has entries and an RSS feed; not much else.  Entries are expected to be in raw html.

## uick start

1. Add "blog" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'blog',
    )

2. Include the blog URLconf in your project urls.py like this::

    url(r'^blog/', include('blog.urls')),

3. Run `python manage.py migrate` to create the blog models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/blog/ to see the blog, or the admin to create entries.
