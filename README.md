# Django-Basic-Blog

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
