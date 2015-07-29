from django.conf import settings
from django.contrib.syndication.views import Feed
from .models import Entry


class EntryFeed(Feed):
    title = getattr(settings, 'BLOG_TITLE', 'My Blog')
    link = '/entries/'
    description = getattr(
        settings, 'BLOG_DESCRIPTION', 'I have a Django Blog!'
    )
    num_results = getattr(settings, 'BLOG_ENTRIES_PER_RSS', 5)

    def items(self):
        return Entry.public.all().order_by('-created')[:self.num_results]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description
