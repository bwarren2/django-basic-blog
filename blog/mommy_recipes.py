from model_mommy.recipe import Recipe, seq
from blog.models import Entry
from django.utils import timezone

entry = Recipe(
    Entry,
    title=seq('Title #'),
    content=seq('Bloggerino #'),
    created=timezone.now,
    modified=timezone.now,
)
