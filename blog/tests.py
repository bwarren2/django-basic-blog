from datetime import timedelta

from django.utils import timezone
from django.test import TestCase

from model_mommy import mommy

from blog.models import Entry


class EntryTestCase(TestCase):

    def setUp(self):
        self.public_entry = mommy.make_recipe(
            'blog.entry', publicity=Entry.PUBLIC
        )
        self.private_entry = mommy.make_recipe(
            'blog.entry', publicity=Entry.PRIVATE
        )

    def test_save_method(self):
        self.public_entry.content = 'Herru'
        self.public_entry.save()
        self.assertGreater(
            self.public_entry.modified,
            timezone.now() - timedelta(seconds=5)  # Hack for time comparison
        )

    def test_public_manager(self):
        public_entries = Entry.public.all().count()
        self.assertEqual(public_entries, 1)

        entries = Entry.objects.all().count()
        self.assertEqual(entries, 2)
