from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from .fields import AutoDatetimeField
from .managers import (
    PublicManager,
    LoginManager,
    PrivateManager,
    PUBLIC,
    LOGIN,
    PRIVATE,
)


class Entry(models.Model):
    PUBLICITIES = (
        (PUBLIC, 'Public'),
        (LOGIN, 'Login'),
        (PRIVATE, 'Private'),
    )
    PUBLIC = PUBLIC
    LOGIN = LOGIN
    PRIVATE = PRIVATE

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default='')  # RSS
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    modified = AutoDatetimeField(default=timezone.now)
    publicity = models.IntegerField(choices=PUBLICITIES, default=PRIVATE)

    class Meta:
        verbose_name_plural = 'entries'

    objects = models.Manager()
    public = PublicManager()
    login = LoginManager()
    private = PrivateManager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:entry', kwargs={'entry_id': str(self.id)})
